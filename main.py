from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton,MDIconButton,MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.textfield import MDTextField
from kivymd.uix.snackbar import Snackbar
from kivy.uix.scrollview import ScrollView

import csv

Window.size = (320,600)

colourb = '56/255,40/255,81/255,1'
colourf = '69/255,55/255,86/255,1'

cardt = """
MDCard:
    radius : dp(15)
    orientation : 'vertical'
    size_hint_y : None
    height : dp(120)
    md_bg_color : 69/255,55/255,86/255,1
    
"""

textt = """
MDTextField:
    tex

"""



filecheck = open('tododat.csv',mode = 'a')
filecheck.close()


class AddItem(MDScreen):
    pass

class Home(MDScreen):
    pass


class TODO(MDApp):
    def clearall(self):       
        csvfile2 = open('tododat.csv','w')
        writer = csv.writer(csvfile2,delimiter = ',')
        writer.writerow([])
        csvfile2.close()
        self.box.remove_widget(self.scroll)
        self.cardfix()
        
    def back(self):
        self.sm.current = 'home'
        self.sm.transition.direction = 'right'
    def addpress(self,arg):
        self.sm.current = 'home'
        self.sm.transition.direction = 'right'
        c = 0
        csvfile = open('tododat.csv','r')
        reader = csv.reader(csvfile,delimiter = ',')
        for row in reader:
            if row != []:
                c = c+1
        csvfile.close()
        if c > 5:
            Snackbar(text = 'ONLY 6 WORKS ALLOWED').open()
            
        else:
            
            L = [self.worktxt.text,self.datetxt.text]
            if L[0] == '':
                pass
            else:
                csvfile2 = open('tododat.csv','a')
                writer = csv.writer(csvfile2,delimiter = ',')
                writer.writerow(L)
                csvfile2.close()
                print(L)
                self.box.remove_widget(self.scroll)
                self.cardfix()
                self.worktxt.text = ''
                self.datetxt.text = ''
        
        
    def addf(self,arg):
        self.sm.current = 'additem'
        self.sm.transition.direction = 'left'
        
        
    
    def deletef1(self,arg):
        l =[]
        csvfile = open('tododat.csv','r')
        reader = csv.reader(csvfile,delimiter = ',')
        for row in reader:
            if row != []:
                l.append(row)
        csvfile.close()
        if len(l) != 0:
            l.pop(0)
            csvfile2 = open('tododat.csv','w')
            writer = csv.writer(csvfile2,delimiter = ',')
            for i in l:
                writer.writerow(i)
            csvfile2.close()
            print(l)
            self.box.remove_widget(self.scroll)
            self.cardfix()
        
        
        
    def deletef2(self,arg):
        l =[]
        csvfile = open('tododat.csv','r')
        reader = csv.reader(csvfile,delimiter = ',')
        for row in reader:
            if row != []:
                l.append(row)
        csvfile.close()
        if len(l) >= 1:
            l.pop(1)
            csvfile2 = open('tododat.csv','w')
            writer = csv.writer(csvfile2,delimiter = ',')
            for i in l:
                writer.writerow(i)
            csvfile2.close()
            print(l)
            self.box.remove_widget(self.scroll)
            self.cardfix()
    def deletef3(self,arg):

        l =[]
        csvfile = open('tododat.csv','r')
        reader = csv.reader(csvfile,delimiter = ',')
        for row in reader:
            if row != []:
                l.append(row)
        csvfile.close()
        if len(l) >= 2:
            l.pop(2)
            csvfile2 = open('tododat.csv','w')
            writer = csv.writer(csvfile2,delimiter = ',')
            for i in l:
                writer.writerow(i)
            csvfile2.close()
            print(l)
            self.box.remove_widget(self.scroll)
            self.cardfix()
    def deletef4(self,arg):

        l =[]
        csvfile = open('tododat.csv','r')
        reader = csv.reader(csvfile,delimiter = ',')
        for row in reader:
            if row != []:
                l.append(row)
        csvfile.close()
        if len(l) >= 3:
            l.pop(3)
            csvfile2 = open('tododat.csv','w')
            writer = csv.writer(csvfile2,delimiter = ',')
            for i in l:
                writer.writerow(i)
            csvfile2.close()
            print(l)
            self.box.remove_widget(self.scroll)
            self.cardfix()
    def deletef5(self,arg):
        l =[]
        csvfile = open('tododat.csv','r')
        reader = csv.reader(csvfile,delimiter = ',')
        for row in reader:
            if row != []:
                l.append(row)
        csvfile.close()
        if len(l) >= 4:
            l.pop(4)
            csvfile2 = open('tododat.csv','w')
            writer = csv.writer(csvfile2,delimiter = ',')
            for i in l:
                writer.writerow(i)
            csvfile2.close()
            print(l)
            self.box.remove_widget(self.scroll)
            self.cardfix()
    def deletef6(self,arg):
        l =[]
        csvfile = open('tododat.csv','r')
        reader = csv.reader(csvfile,delimiter = ',')
        for row in reader:
            if row != []:
                l.append(row)
        csvfile.close()
        if len(l) >= 5:
            l.pop(5)
            csvfile2 = open('tododat.csv','w')
            writer = csv.writer(csvfile2,delimiter = ',')
            for i in l:
                writer.writerow(i)
            csvfile2.close()
            print(l)
            self.box.remove_widget(self.scroll)
            self.cardfix()
    
        
        
    
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette ='DeepPurple'

        self.sm = ScreenManager()
        home = Home(name = 'home')
        home.md_bg_color = 56/255,40/255,81/255,1
        
        additem = AddItem(name = 'additem')
        additem.md_bg_color = 56/255,40/255,81/255,1
        self.sm.add_widget(home)
        self.sm.add_widget(additem)


        #home screen
        self.box = MDBoxLayout(orientation = 'vertical')
        floatbu = MDFloatingActionButton(on_press = self.addf,icon = 'plus',pos_hint = {'right' : 0.95,'center_y' : 0.1})
        floatbu.md_bg_color = 100/255,70/255,110/255,1
        tool1 = MDToolbar(title ='HOME',pos_hint = {'top' : 1})
        tool1.md_bg_color = 100/255,70/255,110/255,1
        tool1.elevation = 10
        tool1.right_action_items = [['delete', lambda x : self.clearall()]]
        

        #cards
        def cardfix():
            self.scroll = ScrollView()
            self.scroll.do_x_scroll = False
            self.grid = MDGridLayout(padding = [15,15,15,35],spacing = 15,cols = 2, size_hint = (1,0.75),pos_hint = {'center_x' : 0.5,'center_y' : 0.5})

            csvfile = open('tododat.csv','r')
            myreader = csv.reader(csvfile,delimiter = ',')
            deletefunct = [self.deletef1,self.deletef2,self.deletef3,self.deletef4,self.deletef5,self.deletef6]
            deleteno = 0
            for row in myreader:
                if row!= []:
                    card = Builder.load_string(cardt)
                    bo2 = MDBoxLayout()
                    bo2.add_widget(Image(source = 'target.png'))
                    bo2.add_widget(MDIconButton(on_press =deletefunct[deleteno] ,icon = 'check-bold',pos_hint = {'top' : 1},user_font_size = '20sp'))
                    card.add_widget(bo2)
                    bo3 = MDBoxLayout(orientation = 'vertical')
                    try:
                        label1 = MDLabel(text = row[0],font_style = 'Subtitle2')
                        label1.halign = 'center'
                        bo3.add_widget(label1)
                    except:
                        pass
                    try:
                        label2 = MDLabel(text = row[1],font_style = 'Caption')
                        label2.halign = 'center'
                        bo3.add_widget(label2)
                    except:
                        pass
                    card.add_widget(bo3)

                    self.grid.add_widget(card)
                    
                    deleteno = deleteno + 1
            self.scroll.add_widget(self.grid)
            self.box.add_widget(self.scroll)
        self.box.add_widget(tool1)
        cardfix()
        self.cardfix = cardfix
        
        





        #add home
        
        

        home.add_widget(self.box)        
        home.add_widget(floatbu)


        #additem screen

        addtool = MDToolbar(title = 'ADD WORKS',pos_hint = {'top' : 1})
        addtool.md_bg_color = 100/255,70/255,110/255,1
        addtool.elevation = 10
        addtool.left_action_items = [['arrow-left',lambda x: self.back()]]
        self.worktxt = MDTextField(size_hint = (0.9,1),pos_hint = {'center_x' : 0.5 , 'center_y' : 0.7})
        self.worktxt.hint_text = 'MENTION THE WORK IN SHORT'
        self.datetxt = MDTextField(size_hint = (0.9,1),pos_hint = {'center_x' : 0.5 , 'center_y' : 0.5})
        self.datetxt.hint_text = 'MENTION THE TIME/DATE IN SHORT'
        
        addbut = MDRaisedButton(text = 'DONE',pos_hint = {'center_x' : 0.5,'center_y' : 0.3},on_press = self.addpress)
        addbut.md_bg_color = 100/255,70/255,110/255,1


        additem.add_widget(addtool)
        additem.add_widget(self.worktxt)
        additem.add_widget(self.datetxt)
        additem.add_widget(addbut)


        

        
        return self.sm

TODO().run()
        
