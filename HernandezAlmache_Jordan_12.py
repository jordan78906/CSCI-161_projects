
#Jordan Hernandez-Alamche
#CSci 161 L03
#Assignment 12

#Class Inheritance(Inheritance, Method Overriding, Super)

class BMW:
   def __init__(self,make,model,year):
      self.make = make
      self.model = model
      self.year = year
   def startEngine(self):
      print('The engine is now on.')
   def stopEngine(self):
      print('The engine is now off.')


class ThreeSeries(BMW):
   def __init__(self,cruiseControlEnabled,make,model,year):
      BMW.__init__(self,make,model,year)
      self.cruiseControlEnabled = cruiseControlEnabled
   def display(self):
      print('\n\nThree Series...')
      print('This {} is a {} of {}'.format(self.make,self.model,self.year))
      if self.cruiseControlEnabled == True:
         super().startEngine()
         print('Button start is on')
      else:
         super().stopEngine()
         print('Button start is off')
      print('--------------------\n\n')


class FiveSeries(BMW):
   def __init__(self,parkingAssistEnabled,make,model,year):
      super().__init__(make,model,year)
      self.parkingAssistEnabled = parkingAssistEnabled
   def display(self):
      print('\n\nFive Series...')
      print('This {} is a {} of {}'.format(self.make,self.model,self.year))
      if self.parkingAssistEnabled != True:
         super().startEngine()
         print('Parking Assists is off')
      else:
         super().stopEngine()
         print('Parking Assists is on')
      print('--------------------')

Make = input('Enter the threeseries make:')
Model = input('Enter Model:')
Year = input(str('Enter Year:'))
cruisechoice = input('Is cruise control on?(y or n):')
cruise_position = True if (cruisechoice == 'y') else False
three_series = ThreeSeries(cruise_position,Make,Model,Year)


Make = input('Enter the fiveseries make:')
Model = input('Enter Model:')
Year = input(str('Enter Year:'))
assistchoice = input('Is parking assist enabled?(y or n):')
assist_position = True if (assistchoice == 'y') else False
five_series = FiveSeries(assist_position,Make,Model,Year)


three_series.display()
five_series.display()

