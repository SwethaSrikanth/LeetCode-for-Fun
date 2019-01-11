# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:25:34 2018

@author: Swetha Srikanthan
"""

#Easy
#929: Unique Email Address

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        elist = []
        for item in emails:
            if item.count('@') == 1:
                #process local part of the email
                local,domain = (item.split('@'))
                #for more than one occurance of + 
                localy = local.split('+')
                #or leet has ->>> local = local[:local.index('+')]
                local = localy[0].replace('.','')
                #append the domain
                email = local +'@'+domain
                elist.append(email)
                #print(len(set(elist)))
        return len(set(elist))
                
            
            
if __name__ == "__main__":  
    #emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    emails = ["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]
    a = Solution()
    print(a.numUniqueEmails(emails))
    
