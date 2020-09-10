import json
import datetime
import hashlib



class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_block(proof=1,previous_hash='0')
    def create_block(self,proof,previous_hash):
        block={'index': len(self.chain)+1,
                'timestamp': str(datetime.datetime.now()),
                'proof': proof,
                'prev_hash':previous_hash}
        self.chain.append(block)
        return block

    #get previous Block
    def get_previous_block(self):
        return self.chain[-1]
    #proof of work
    def proof_of_work(self,previous_proof):
        new_proof=1
        check_proof=False

        while check_proof is False:
            val1=new_proof**2
            val2=previous_proof**2
            #print(type(val1))
            #print(type(val2))
            hash_op=hashlib.sha256(str(val1-val2).encode()).hexdigest()


            if hash_op[:4]=='0000':
                check_proof=True
            else:
                #check for further correct hash
                new_proof+=1
        print(new_proof)
        print(type(new_proof))
        return new_proof


    #encode previous block to hash fun
    def hash(self,block):
        encoded_block=json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self,chain):
        prev_block_index=0
        curr_block_index=1

        while curr_block_index < len(chain):
            curr_block=chain[curr_block_index]
            prev_block=chain[prev_block_index]

            #check if prev hash matches prev hash of curr block_index
            if block['prev_hash'] != hash(prev_block):
                return False

            #check if hash value starts with '0000'
            prev_proof=prev_block['proof']
            curr_proof=curr_block['proof']
            hash_op=hashlib.sha256(str(curr_proof**2-prev_proof**2).encode()).hexdigest()

            if hash_op[:4] != '0000':
                return False

            #set previous index and curr block_index
            prev_block_index=curr_block_index
            curr_block_index+=1

        return True

    def __str__(self):
        print(len(chain))
        return len(chain)


#blockchain= Blockchain()
#print(len(blockchain.chain))
#previous_block=blockchain.get_previous_block()
#previous_proof=previous_block['proof']

#blockchain.proof_of_work(previous_proof)
