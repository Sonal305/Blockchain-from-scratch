from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from app import blockchain

import json

#add a block
obj = blockchain.Blockchain()
def mine_block(request):
    previous_block=obj.get_previous_block()
    print(previous_block)
    previous_proof=previous_block['proof']
    #print(type(previous_proof))
    proof=obj.proof_of_work(previous_proof)
    previous_hash=obj.hash(previous_block)
    block=obj.create_block(proof,previous_hash)

    response = {
    'message' : 'Congrats! Successfully Mined',
    'index' : block['index'],
    'timestamp': block['timestamp'],
    'proof': block['proof'],
    'previous_hash': block['prev_hash'],
    }

    return JsonResponse(response)


def getchain(request):

    response={
    'chain':  obj.chain,
    'length': len(obj.chain),
    }
    return JsonResponse(response)
