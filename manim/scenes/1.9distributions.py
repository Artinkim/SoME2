from manim import *
from scipy import linalg

def CreateDistributionGraph1(): # these graphs are hard coded bc coordinates are weird for bar graphs
    line = NumberLine(
            x_range=[0.1, 5, 101],
            length=10,
            color=BLUE,
            include_numbers=True,
        ).set_x(-0.5).set_y(-2) # hardcoded

    def curve(x):
        return 0.5*np.pi*x*np.exp(-0.25*np.pi*x*x)

    return FunctionGraph(lambda x: curve(line.p2n((x,0,0)))*5).move_to(line) # hardcoded

def CreateDistributionGraph2(): # these graphs are hard coded bc coordinates are weird for bar graphs
    line = NumberLine(
            x_range=[0.1, 5, 101],
            length=10,
            color=BLUE,
            include_numbers=True,
        ).set_x(0.2).set_y(1.2) # hardcoded

    def curve(x):
        return np.exp(-x)

    return FunctionGraph(lambda x: curve(line.p2n((x,0,0)))*2.2).move_to(line) # hardcoded

class Distribution1(Scene):
    def construct(self):
        N = 2 # size of matrix   
        niter = 5000 # number of samples
        evals = np.zeros((niter,N))
        delta = np.zeros((niter,N-1))
        histograms = np.zeros((niter,100))
        for n in range(niter):
            M_temp = np.random.randn(N,N)
            M = (M_temp + M_temp.T)/2
            M = M/np.sqrt(N)
            evals[n,:] = linalg.eigvalsh(M)
            delta[n,:] = evals[n,1:]-evals[n,:-1]
            histograms[n,:] = np.histogram(delta/np.mean(delta),bins=np.linspace(0.1, 5,101),density=True)[0]

        chart = BarChart(values=histograms[-1])
        func = CreateDistributionGraph1()
        decimal = Integer(0)
        t = ValueTracker(0)
        
        chart.add_updater(lambda c: c.change_bar_values(histograms[int(t.get_value())]))
        decimal.add_updater(lambda x: x.set_value(t.get_value()+1))

        self.add(chart,decimal)
        self.play(t.animate(rate_func=smooth).set_value(niter-1),run_time=5)
        self.play(Create(func),run_time=2)
        self.wait(1)
  
class Distribution2(Scene):
    def construct(self):
        N = 5000 # size of matrix   
        niter = 1 # number of samples
        evals = np.zeros((niter,N))
        delta = np.zeros((niter,N-1))
        histograms = np.zeros((niter,100))
        for n in range(niter):
            M_temp = np.random.randn(N,N)
            M = (M_temp + M_temp.T)/2
            M = M/np.sqrt(N)
            evals[n,:] = linalg.eigvalsh(M)
            delta[n,:] = evals[n,1:]-evals[n,:-1]
            histograms[n,:] = np.histogram(delta/np.mean(delta),bins=np.linspace(0.1, 5, 101),density=True)[0]

        chart = BarChart(values=histograms[-1])
        func = CreateDistributionGraph1()
        
        self.add(chart)
        self.play(Create(func),run_time=2)
        self.wait(1)

class Distribution3(Scene):
    def construct(self):
        N = 5000 # size of matrix   
        niter = 100 # number of samples
        evals = np.zeros((niter,N))
        delta = np.zeros((niter,N-1))
        histograms = np.zeros((niter,100))
        for n in range(niter):
            evals[n,:] = np.sort(np.random.uniform(-N/2,N/2,N))
            delta[n,:] = evals[n,1:]-evals[n,:-1]
            histograms[n,:] = np.histogram(delta/np.mean(delta),bins=np.linspace(0.1, 5, 101),density=True)[0]

        chart = BarChart(values=histograms[-1])
        func = CreateDistributionGraph2()
        decimal = Integer(0)
        t = ValueTracker(0)
        
        chart.add_updater(lambda c: c.change_bar_values(histograms[int(t.get_value())]))
        decimal.add_updater(lambda x: x.set_value(t.get_value()+1))

        self.add(chart,decimal)
        self.play(t.animate(rate_func=smooth).set_value(niter-1),run_time=5)
        self.play(Create(func),run_time=2)
        self.wait(1)
  
        

