#!/usr/bin/env python
# coding: utf-8

# In[5]:


from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello':'World'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id':item_id, 'q':q}


