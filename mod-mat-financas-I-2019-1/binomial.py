#################################################################################
#
# Project           : University Courses / Modelagem Matemática em Finanças I
#
# Program name      : binomial.py
#
# Author            : gilmiranda
#
# Date created      : 03-30-2019
#
# Purpose           : Take a binomial one step tree with initial values and two final values
#                     and discretize for an arbitrary time 't'
#
# Revision History  :
#
# Date          Author          Ref    Revision (Date in MM-DD-YYYY format)
# 03-30-2019    gilmiranda      1      Created.
# 03-31-2019    gilmiranda      2      Bug-fix no calc_Vs, agora o algoritmo
#                                      calcula corretamente o V_0, ou valor justo
#
#################################################################################

class binomial:
    def __init__(self):
        self.Sf = [0,0] ## Guarda os valores finais da binomial inicial
        self.Sf_disc = [] ## Guarda os valores finais da multinomial, já discretizada
        self.Vs = [] ## Matriz com todos os Vs ao longo do tempo na árvore, sendo o indíce n de cada vetor, seu t_n
        self.Vf = []
        self.ts = 1 ## Tempo a ser discretizado
        self.s0 = 10 ## Valor inicial da árvore
        self.u = self.Sf[0]/self.s0 ## Up factor inicial
        self.d = self.Sf[1]/self.s0 ## Down factor inicial
        self.r = 1/10 ## Taxa de juros
        self.k = 1 ## Strike da opção call/put
        self.u_disc = 1
        self.d_disc = 1
        self.ptil = 1
        self.qtil = 1

    def set_k(self, k): ## Seta strike
        self.k = k

    def set_Sf(self,s): ## Seta Sf
        self.Sf[0] = s[0]
        self.Sf[1] = s[1]

    def set_s0(self,s): ## Seta S0
        if s == 0: raise ValueError('Preço inicial 0 não será modelado')
        self.s0 = s

    def set_Ts(self,t):
        self.ts = t

    def set_riskneutral(self):
        self.ptil = ((1+self.r)-self.d_disc)/(self.u_disc - self.d_disc)
        self.qtil = 1-self.ptil

    def set_factors(self):
            self.u_disc =((self.Sf[0]/self.s0)**(1/(self.ts-1)))
            self.d_disc = ((self.Sf[1]/self.s0)**(1/(self.ts-1)))

    def discretize(self):
        self.Sf_disc = []
        for i in range(0,self.ts):
            self.Sf_disc.append(self.u_disc**(self.ts-1-i)*self.d_disc**(i)*self.s0)

    def print_Sf(self):
        print(self.Sf_disc)

    def call(self, s):
        if self.k >= s: return 0
        return s - self.k

    def put(self, s):
        if s >= self.k: return 0
        return self.k - s

    def set_Vf(self, f):
        self.Vf = [f(i) for i in self.Sf_disc]

    def calcprev_V(self,Vnxt):
        return (1/(1+self.r))*(Vnxt[0]*self.ptil + Vnxt[1]*self.qtil)

    def calc_Vs(self):
        self.Vs.append(self.Vf)
        for j in range(0,self.ts-1):
            aux = []
            c = len(self.Vs[-1])
            for i in range(0,c-1):
                aux.append(self.calcprev_V((self.Vs[-1][i],self.Vs[-1][i+1])))
            self.Vs.append(aux)
        self.Vs = self.Vs[::-1]
