
import csnd6
orc = """
nchnls=2
instr   1 
  aoutl  oscil 32000,512,1
  aoutr = aoutl
  outs aoutl,aoutr
endin
"""
sco ="""
f1 0 16384 10 1
i 1 0 4
"""
c = csnd6.Csound()
c.SetOption("-omelanges.wav") 
c.CompileOrc(orc)
c.ReadScore(sco) 
c.Start()
c.Perform() 
c.Stop()
