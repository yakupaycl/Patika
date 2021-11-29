#!/usr/bin/env python
# coding: utf-8

# In[ ]:


[16,21,11,8,12,22] -> Merge Sort

get_ipython().set_next_input('1. Yukarıdaki dizinin sort türüne göre aşamalarını yazınız');get_ipython().run_line_magic('pinfo', 'yazınız')

                        [16,21,11,8,12,22]
    
                     ([16,21,11], [8,12,22])
                    ([16,21], [11], [8,12], [22])
                 (\, /, [16], [21], [11], [8], [12], [22])
              \    \   /                   \    \    /
             [16,21] [11]                  [8,12] [22]
                \     /                      \      /
              [11,16,22]                    [18,12,22]
                    \                          /
                         [8,11,12,18,21,22]
                    


# In[ ]:


get_ipython().set_next_input('2.Big-O gösterimini yazınız');get_ipython().run_line_magic('pinfo', 'yazınız')
  
    O(nlogn)

