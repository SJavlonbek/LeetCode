def convertTime(current, correct):
        h1,m1=current.split(":")
        h2,m2=correct.split(":")
        h1=int(h1)
        h2=int(h2)
        m2=int(m2)
        m1=int(m1)
        s=(h2-h1)*60+(m2-m1)
        z=0
        if s//60:
            z+=s//60
            s=s-60*(s//60)
        if s//15:
            z+=s//15
            s=s-15*(s//15)
        if s//5:
            z+=s//5
            s=s-5*(s//5)
        if s>0:
            z+=s
            s=0
        return z