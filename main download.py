
from cgitb import text
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton,MDRectangleFlatButton,MDFlatButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDTextButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import TwoLineListItem,MDList,TwoLineIconListItem
from pytube import YouTube
from tkinter import filedialog 
from kivymd.uix.filemanager import MDFileManager

from plyer import filechooser




Window.size=(400,600)

file_path="""
MDFloatLayout:
    MDRaisedButton:
        text:"Set the download path"
        
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_release:app.file_chooser()
"""



#........................Logo........................................
img="""
Image:
   
    image_size:"40sp"
    source:"logo.png" 
    pos_hint:{'center_x':0.5,'center_y':0.8}
    """


#...........................textinput.................................
username_helper = """

MDTextField:
    id:google_enter
    hint_text:"Paste the video Link"
    helper_text:'Click Audio or Video Button to Download'
    helper_text_mode:"on_focus"
    icon_right:"youtube"

    pos_hint:{'center_x':0.5,'center_y':0.6}
    size_hint_x:None
    width:300
"""




class VidApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Yellow"
        screen=Screen()
        self.user = Builder.load_string(username_helper)
        image=Builder.load_string(img)
        download_path=Builder.load_string(file_path)
        
        
        video_btn=MDFillRoundFlatButton( text="Video Download",text_color=(246/255,0,33/255,1),size_hint=(.4,None)
                     ,font_size="17sp",font_name="Comic",pos_hint={'center_x':0.5,'center_y':0.5}
                   ,on_release=self.show_data)
        audio_btn=MDFillRoundFlatButton( text="Audio Download",text_color=(50/255, 62/255, 231/255,1),
                      pos_hint={'center_x':0.5,'center_y':0.4},size_hint=(.4,None),
                      font_name="comic",font_size="17sp" ,on_release=self.show_data1)
        label1=MDLabel(  text="Best Youtube Downloader app ",pos_hint={'center_x':0.75,'center_y':0.1},text_size="20sp",font_style="Subtitle2")
        label2=MDLabel(   text="To Download your favorite videos (or) audio on youtube", pos_hint={'center_x':0.6,'center_y':0.07}
                ,font_style="Caption",font_size="12sp")
        label3=MDLabel(   text="play it and enjoy it",pos_hint={'center_x':0.5,'center_y':0.05},halign="center",
                font_style="Caption",font_size="12sp")
        
        screen.add_widget(label1)
        screen.add_widget(label2)
        screen.add_widget(label3)
      
        screen.add_widget(image)
        screen.add_widget(self.user)
        screen.add_widget(download_path)
        screen.add_widget(video_btn)
        screen.add_widget(audio_btn)
      
    

        return screen

#......................................Video download.........................................
    def show_data(self,*args):
        
        if self.user.text is "":
            check1 = "plese enter the video link"


        else:
            check1 = self.user.text

        close = MDFlatButton(text="close",on_release=self.close)
        btn2 = MDFlatButton(text="Resulution",on_release=self.vid_download)
      
        self.dialog = MDDialog(title="Youtube downloder", text=check1, size_hint=(0.7, 1), buttons=[close, btn2])
        self.dialog.open()


    def close(self, obj):
        self.dialog.dismiss()
    
    def vid_download(self,obj):

        link=self.user.text
        self.youtube=YouTube(link)
        print(link)
        #youtube.streams.get_highest_resolution().download(self.selected_path)
        
        btn1 = MDRaisedButton(text="720p",on_release=self.high)
     
        btn3 = MDRaisedButton(text="360p",on_release=self.low )
        btn4 = MDRaisedButton(text="cancel",on_release=self.exit )
        self.dialog1 = MDDialog(title="Youtube downloder",  size_hint=(0.8,.95), buttons=[btn1,btn3,btn4])
        self.dialog1.open()
    def exit(self,obj):
        self.dialog1.dismiss()   


#....................................video download opption..............................
    def high(self,obj):
        videos=self.youtube.streams.all()
        vid=list(enumerate(videos))
        for i in vid:
           print(i)
        print()
        strm=2
        videos[strm].download(self.selcted_path)
        sucess=Snackbar(text="Video Download Sucessfull")
        sucess.open()

    

    
    def low(self,obj):
        videos=self.youtube.streams.all()
        vid=list(enumerate(videos))
        for i in vid:
           print(i)
        print()
        strm=1
        videos[strm].download(self.selcted_path)
        sucess=Snackbar(text="Video Download Sucessfull")
        sucess.open()





        
#https://www.youtube.com/watch?v=L0glXBZPd1Q

#......................................file_path..............................................................
    
    def file_chooser(self):
        path=filedialog.askdirectory()
        print(path)
        self.selcted_path=path
        #filechooser.open_file(on_selection=self.selected)
       
    #def selected(self,selection):
        #self.selected_path=selection
        #print(self.selected_path)
       

#........................................audio_download...............................................
    def show_data1(self,obj):
        if self.user.text is "":
            check1 = "plese enter the video link"


        else:
            check1 = self.user.text

        close = MDFlatButton(text="close",on_release=self.close)
        btn2 = MDFlatButton(text="Download",on_release=self.audio_download)
      
        self.dialog = MDDialog(title="Youtube downloder", text=check1,size_hint=(0.7, 1), buttons=[close, btn2])
        self.dialog.open()

    
    def close(self, obj):
        self.dialog.dismiss()
    def audio_download(self,obj):

        link=self.user.text
        youtube=YouTube(link)
        print(link)
        videos=youtube.streams.filter(only_audio=True)
        vid=list(enumerate(videos))
        for i in vid:
           print(i)
        print()
        strm=1
        videos[strm].download(self.selcted_path)
        sucess=Snackbar(text="Audio Download Sucessfull")
        sucess.open()
     

 

VidApp().run()



#https://www.youtube.com/watch?v=scvAlr8VG-g

#def file_chooser(self):
        #path=filedialog.askdirectory()
        #print(path)
        #filechooser.open_file(on_selection=self.selected)
       
    #def selected(self,selection):
        #self.selected_path=selection
        #print(self.selected_path)