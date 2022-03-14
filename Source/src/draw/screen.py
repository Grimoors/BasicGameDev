'''
Class VPixel
===========

This Class defines a Virtual Pixel.

An Individual Pixel is defined as a set of (BackGroundColor, ForeGroundColor , ForeGroundCHar)


Member Functions - 
--------------------
- Constructor 
-- default -> (self)- Declares and sets R,G,B values of 1 Vpixel to ("black","black"," ") - True Black



- _PixArray -> (noOfPixels) - Returns a Linear Array of noOfPixels Length - Used to define Screens and Other Entity Sprites

- updateVpixel( self, BGC, FGC, FGCH)
Updates BGC, FGC, FGCH of an individual pixel in a VScreen Object

- colorprint -> (pixel) - Upon being given a Pixel as an input, returns the Escape Sequence needed to render that pixel using print( EscSequence , end = '')

'''


class VPixel:
    # Constructor
    def __init__(self) -> None:
        self.BGC = "black"
        self.FGC = "black"
        self.FGCH = " "
        self.FRMT = "unformatted"
        pass

    #Return an Array of Pixels
    def _PixArray( noOfPixel) :
        return [VPixel() for i in range(noOfPixel)]
        # pass

    def updateVpixel( self, BGC, FGC, FGCH, FRMT ):
        self.BGC = BGC
        self.FGC = FGC
        self.FGCH = FGCH
        self.FRMT = FRMT
        pass

    def colorprint(pixel):
        ''' 
Colors the text according to the given color
The color can be one of the 'COLORS' in the array 'COLORS' or can be explicitly mentioned using ASCII color codes.
'''     
        COLORS ={
            'blackText':'30',
            'redText':'31',
            'greenText':'32',
            'yellowText':'33',
            'blueText':'34',
            'purpleText':'35',
            'cyanText':'36',
            'whiteText':'37',
            'black':'40',
            'red':'41',
            'green':'42',
            'yellow':'43',
            'blue':'44',
            'purple':'45',
            'cyan':'46',
            'white':'47',
        }
        FORMAT={
            "unformatted":"0",
            "normal":"22",
            "bold":"1",
            "faint":"2",
            "italic":"3",
            "underline":"4",
            "slowblink":"5",
            "rapidblink":"6",
            "reverseColors":"7",
            "dim":"8",
            "strikethrough":"9",
            "bolditalic":"1;3",
            "boldunderlined":"1,4",
            "boldstrikethrough":"1;9",
            "italicstrikethrough":"3;9",
            "bolditalicstrikethrough":"1;3;9",
        }
        bgc = pixel.BGC
        fgc = pixel.FGC
        char = pixel.FGCH
        frmt = pixel.FRMT 
        END_COLOR = '\033[m'
        try:
            return "\x1b["+FORMAT[frmt]+";"+ COLORS[fgc]+";"+COLORS[bgc]+"m" + char + END_COLOR
        except:
            return char
        pass


'''
Class Vscreen
=============

This class defines a Virtual Screen.

A individual Virtual Screen has attributes - int height, int  width, Vpixel ScreenGrid[]

Member Methods -
----------------

-Constructor -> (self, int height, int width) - Takes input of hright and width and defines a Screen, with a Linear Array of (height * width) Vpixels.

- updateScreenGrid ( Vscreen Destination_Screen, Vscreen Source_Screen) -> Copies Grid of Source to the grid of Destination. Assumes Screen sizes are same.

- displayScreen( self ) - Prints out the Grid of the current VScreen. Effectively a Visual Getter Function 

'''

class Vscreen:
    def __init__(self,height,width) -> None:
        self.screenGrid = VPixel._PixArray( noOfPixel = height*width)
        self.height = height
        self.width = width 
    
    
    def updateScreenGrid (Destination_Screen, Source_Screen):
        for i in range (Destination_Screen.height * Destination_Screen.width ):
            Destination_Screen.screenGrid[i] = Source_Screen.screenGrid[i] 
        pass

    def renderState (self, state ):  
        self.updateScreenGrid (self.screenGrid , state.background() )
        self.updateScreenGrid(self.screenGrid , state.entityLayerGrid() )

    def displayScreen(self):
        print()
        for y in range (self.height) :
            for x in range (self.width) :
                print (VPixel.colorprint(self.screenGrid[x+y*self.width]) , end="")
            print()
        pass

'''
Class VPixelTypes
=================

This Class is a Container for Different Formats of Pixels that we will use. 
'''
class VPixelTypes:

    Border ={
        "BGC":"white",
        "FGC":"blackText",
        "FGCH":"-",
        "FRMT":"bold"
    }

    YellowTextBlackBG ={
        "BGC":"cyan",
        "FGC":"redText",
        "FGCH":"",
        "FRMT":"unformatted",
    }

    Template ={
        "BGC":"",
        "FGC":"",
        "FGCH":"",
        "FRMT":"",
    }

class StaticDraws:
    
    def DefaultBorder(screenIn,asy,asx):
        screen = screenIn
        latthickness =  int ( screen.width / 10 )  if  (int ( screen.width / 10 ) < asx ) else asx 
        verthickness = int ( screen.height / 10 ) if ( int ( screen.height / 10 ) < asy ) else asy
        
        px = VPixelTypes.Border

        for y in range(verthickness):
            for x in range(screen.width):
                screen.screenGrid[x+y*screen.width].updateVpixel(   px.get("BGC"), px.get("FGC") , px.get("FGCH") ,px.get("FRMT") )
        for y in range (verthickness, screen.height - verthickness):
            for x in range(latthickness):
                screen.screenGrid[x+y*screen.width].updateVpixel(px.get("BGC"), px.get("FGC") , px.get("FGCH"),px.get("FRMT") )
            for x in range(screen.width - latthickness, screen.width):
                screen.screenGrid[x+y*screen.width].updateVpixel(px.get("BGC"), px.get("FGC") , px.get("FGCH"),px.get("FRMT") )
        for y in range(screen.height - verthickness , screen.height):
            for x in range(screen.width):
                screen.screenGrid[x+y*screen.width].updateVpixel(px.get("BGC"), px.get("FGC") , px.get("FGCH"), px.get("FRMT") )
        return screen

    def displayXCentredText (screenIn, Text, pixelType, y = 2 ):
        k = len( Text)
        px = pixelType
        i=0
        for x in range ( int (screenIn.width/2) - int(k/2) , int (screenIn.width/2) + int(k/2) + 1 ):
            screenIn.screenGrid[x+y*screenIn.width].updateVpixel( px.get("BGC"), px.get("FGC") , Text[i] ,px.get("FRMT"))
            i+=1
        return screenIn
    
    def TitleDisplay(screenIn):
        return StaticDraws.displayXCentredText( screenIn , "Clash of Clans - BareBones Edition - 2020113002" , VPixelTypes.YellowTextBlackBG , y= 2)


        


if __name__ == '__main__' :
    def tester_Screen():
        Screen = Vscreen (60,200)
        Screen.updateScreenGrid(StaticDraws.DefaultBorder(Screen,5,3))
        # Screen.displayScreen()
        Screen.updateScreenGrid( StaticDraws.TitleDisplay( screenIn = Screen) )
        Screen.displayScreen()
    
    tester_Screen()
    def tester_VPixel_colorprint1():
        print()
        Array = VPixel._PixArray(10)
        for Pixel in Array:
            print ( VPixel.colorprint( Pixel) , end="")    
    # tester_VPixel_colorprint1()