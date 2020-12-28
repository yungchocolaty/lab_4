class Gang:

    def __init__(self, rep):

        self.rep = rep

    def show_info(self):
        print("Hi feller, my name is " + self.name, ", I am a " + str(self.rep))

    def action(self):
        print("I am...")


class Dutch(Gang):

    def __init__(self, name, money, rep):
        super().__init__(rep)
        self.name = name
        self.money = money

    def show_info(self):
        super().show_info()
        print("My gang needs one last job, some commotion and", str(self.money), 'dollars')
        print("remember, I always have a plan")

    def action(self):
        super().action()
        print("thinking(doing nothing)")


class John(Gang):

    def __init__(self,name,rep, horse):
        super().__init__(rep)
        self.name = name
        self.horse = horse


    def show_info(self):
        super().show_info()
        print("I've just robber a feller ant took his", self.horse, 'horse.')
        print("My side ain't chosen. My side was given")

    def action(self):
        print('If you say so')
        print('Bang')


class Gun():

    def __init__(self, condition, revolver, damage):
        self.condition = condition
        self.revolver = revolver


        self.damage = damage

    def show_info(self):
        print("Arthur's favourite", str(self.revolver),  "in", str(self.condition),
              "condition, enough damage for", str(self.damage))

    def action(self):
        print("Bang!")


class Arthur(Gun):

    def __init__(self, experience, revolver, condition, damage):
        super().__init__(revolver, condition, damage)

        self.experience = experience

    def show_info(self):

        print("I'm Arthur, Dutch's",str(self.experience))
        print('We’re thieves, in a world that doesn’t want us no more')
        print("We shoot fellers as need shooting, save fellers as need saving, and feed 'em as need feeding.")
        print("Take a look at my revolver")
        super().show_info()


    def action(self):
        super().action()
        print("I never asked for this.") #I know it's a different game

