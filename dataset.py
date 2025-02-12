import torch
import torch.nn as nn
from torch.utils.data import Dataset

class BilingualDataset(Dataset):

    def __init__(self,ds,tokenizer_src,tokenizer_tgt,src_lang,tgt_lang,seq_len) -> None:
        super().__init__()

        self.ds = ds
        self.tokenizer_src = tokenizer_src
        self.tokenizer_tgt  = tokenizer_tgt
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang

        self.sos_token = torch.Tensor([tokenizer_src.token_to_id(['SOS'])],dtype = torch.int64)
        self.eos_token = torch.Tensor([tokenizer_src.token_to_id(['EOS'])],dtype = torch.int64)
        self.pad_token = torch.Tensor([tokenizer_src.token_to_id(['PAD'])],dtype = torch.int64)


    