from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value


class NFT:

    def __init__(self, value = 0, newOwner = NULL, currentOwner = NULL):
        self.value = value # current value of NFT at purchase
        self.newOwner = newOwner # the buyer
        self.currentOwner = currentOwner # current holder
        # after transaction, newOwner should be null (i think) and currentOwner should be the buyer
        # should be a swap method with the extra stuff that sends these changes to frontend (i think)

    def processTransaction(wallet):
        print("NFT Transaction Processing...")
        if (wallet >= NFT.value): #i forgot to define the wallet somewhere, but basically it's just how much money you have to buy the nft
            wallet = wallet - NFT.value
            temp = newOwner
            currentOwner = newOwner
            newOwner = NULL # i think
            temp = NULL
            print("Transaction complete, get scammed idiot")
        else:
            print("Insufficent funds lmao")
# so this is basically the transaction function, not quite sure yet how to send the info
# to frontend, but the base code is here