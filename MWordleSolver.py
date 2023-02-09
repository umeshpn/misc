import wordle
class MWordleSolver(wordle.WordleSolver):
    def __init__(self):
        mdict = [
            "aalam", "maram", "panni", "makan", "lokam", "mlaav", "vaava", "mazha", "kinar", "kuzhi", "muyal", "thiri",
            "petti", "kanni", "vaaka", "kizhi", "melam", "lolan", "pavan", "anali", "madhu", "chila", "vazhi", "jilla",
            "dveep", "jalam", "sabha", "thala", "vidya", "balam", "mutta", "vanam", "jaiva", "puzha", "paatt", "rasam",
            "param", "pakal", "kayar", "mayil", "tholi", "jeevi", "mashi", "nayam", "theng", "kanam", "varav", "naaya",
            "kaaya", "kamal", "janmi", "gathi", "valam", "maala", "chevi", "palli", "kooli", "paamp", "dhanu", "yugam",
            "kriya", "varam", "maapp", "mozhi", "appam", "mikav", "neeli", "veyil", "mulla", "vayal", "ruchi", "pizha",
            "nanma", "konna", "vaaya", "vayar", "vishu", "payar", "urukk", "illam", "potti", "appan", "kappa", "chuma",
            "karam", "janam", "manam", "vanya", "vaiki", "malar", "plaav", "soura", "thekk", "jayam", "chiri", "poyka"
        ]
        super().__init__(5)
        self.set_dictionaries(mdict, [])


        