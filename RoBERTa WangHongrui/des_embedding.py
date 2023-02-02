import torch
from tqdm import tqdm
from dataset_tool import fast_merge
import numpy as np
from transformers import pipeline, T5Tokenizer, T5EncoderModel
import os

user,tweet=fast_merge(dataset="") #datasetname

user_text=list(user['description'])
tweet_text = [text for text in tweet.text]


feature_extract=pipeline('feature-extraction',model='roberta-base',tokenizer='roberta-base',device=2,padding=True, truncation=True,max_length=50)

def Des_embbeding():
        print('Running feature1 embedding')
        path=""
        if not os.path.exists(path):
            des_vec=[]
            for k,each in enumerate(tqdm(user_text)):
                if each is None:
                    des_vec.append(torch.zeros(512))
                else:
                    feature=torch.Tensor(feature_extract(each))
                    for (i,tensor) in enumerate(feature[0]):
                        if i==0:
                            feature_tensor=tensor
                        else:
                            feature_tensor+=tensor
                    feature_tensor/=feature.shape[1]
                    des_vec.append(feature_tensor)
                    
            des_tensor=torch.stack(des_vec,0)
            torch.save(des_tensor,path)
        else:
            des_tensor=torch.load(path)
        print('Finished')
        return des_tensor


Des_embbeding()
