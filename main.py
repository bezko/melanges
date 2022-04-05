
import csnd6
orc = """
nchnls=2
instr   1 

  aenv   linseg 0,1/64,1,p3-1/32,1,1/64,0
  aoutl  oscil aenv*8000,p4,1
  aoutr = aoutl
  outs aoutl,aoutr
endin
"""
sco ="""
f1 0 16384 10 1
i 1 0 .25 512
i 1 0.25 .25 739.932
i 1 0.8052451659746271 .25 1299.5081801643348
i 1 1.1387886347566916 .25 1613.8043853904758
"""
c = csnd6.Csound()
c.SetOption("-omelanges.wav") 
c.CompileOrc(orc)
c.ReadScore(sco) 
c.Start()
c.Perform() 
c.Stop()
