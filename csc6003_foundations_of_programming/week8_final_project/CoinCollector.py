# Importing dependencies
from typing import List
from typing import Tuple

# This class mimics a coin counter machine
class CoinCollector:
    # constructor so you cannot instantiate this class
    def __init__(self):
        raise TypeError("You cannot instantiate this class.")
        
    # Making parse change a static method since it does not use anything in the class
    @staticmethod
    def parseChange(coins: str) -> Tuple[int, List]:
        # dictionary to hold change conversion map
        coin_values: dict = {
            "p": 1,
            "n": 5,
            "d": 10,
            "q": 25,
            "h": 50,
            "w": 100,
        }

        # tracking invalid coins
        invalid_coins: List = []
        # coin counter
        coin_counter: int = 0
        # splitting string into list
        coins: list = list(coins)
        # calculating coin total
        for coin in coins:
            # If coin is invalid, add it to invalid list other wise count it
            if coin not in coin_values:
                # ad invalid coin to list
                invalid_coins.append(coin)
            else:
                # counting coins
                coin_counter += coin_values[coin]
        return coin_counter, invalid_coins

