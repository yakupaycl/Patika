#!/usr/bin/env python
# coding: utf-8

# In[ ]:


[22,27,16,2,18,6] >- Insertion Sort


# In[ ]:


1. Yukarı verilen dizinin sort türüne göre aşamalarını yazınız ?

    1. [22,27,16,2,18,6] n
    2. [2,27,16,22,18,6] n-1
    3. [2,6,16,22,18,27] n-2
    4. [2,6,16,18,22,27] n-3


# In[ ]:


get_ipython().set_next_input('2. Big-O gösterimini yazınız');get_ipython().run_line_magic('pinfo', 'yazınız')
o(n²)


# In[ ]:


3. Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, 
    get_ipython().set_next_input('    Best case: Aradığımız sayının dizinin en başında olması');get_ipython().run_line_magic('pinfo', 'olması')

    .Average Case: n²
    .Worst Case: n
    .Best Case : n²


# In[ ]:


4.Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.

18 sayısı Average Case kapsamına girer.


# In[ ]:


5. [7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.

    1. [7,3,5,8,2,9,4,15,6] n
    2. [2,3,5,8,7,9,4,15,6] n-1
    3. [2,3,4,8,7,9,5,15,6] n-2
    4. [2,3,4,5,7,9,8,15,6] n-3
    5. [2,3,4,5,6,9,8,15,7] n-4
    6. [2,3,4,5,6,7,8,15,9] n-5
    7. [2,3,4,5,6,7,8,9,15] n-6

