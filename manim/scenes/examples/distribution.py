from manim import *
from scipy import linalg


class dis1(Scene):

    def getVals(self,N):
        M_temp = np.random.randn(N,N)
        M = (M_temp + M_temp.T)/2
        M = M/np.sqrt(N)
        evals = linalg.eigvalsh(M)
        return evals


    def construct(self):
        charts = [(BarChart(values = self.getVals(int(N)),x_length = 10),print(N)) for N in np.arange(2,10,0.2)] 

        time = 3
        for i in range(len(charts)-1):
            self.play(ReplacementTransform(charts[i], charts[i+1]),run_time = time/len(charts))
  