class cannon:
    def __init__(self) -> None:
        self.attriDict={
            "hp":"100",
            "atk":"15",
            "def":"15",
            "atkfreq":"0.5",
            "type":"defbuild"
        }
        self.displayDict={
            "BGC":"black",
            "FGC":"white",
            "FGCH":"x",
            "FRMT":"bold",
        }
        self.currHp = self.attriDict.get("hp")
        self.type = "defbuild"
        self.name = "cannon"
        
