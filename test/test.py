from functional import seq
import itertools
mouse_dx_all = ["dx.mouse.position.lock.api",
                "dx.mouse.position.lock.message",
                "dx.mouse.focus.input.api",
                "dx.mouse.focus.input.message",
                "dx.mouse.clip.lock.api",
                "dx.mouse.input.lock.api",
                "dx.mouse.state.api",
                "dx.mouse.state.message",
                "dx.mouse.api",
                "dx.mouse.cursor",
                "dx.mouse.raw.input",
                "dx.mouse.input.lock.api2",
                "dx.mouse.input.lock.api3",
                ]
mouse_type_list = seq(range(1,len(mouse_dx_all)+1)) \
    .flat_map(lambda n:itertools.combinations(mouse_dx_all,n))
print(mouse_type_list[20])
# import win32api
# import win32con
# import time
#
# time.sleep(2)
# win32api.keybd_event(win32con.VK_NUMPAD7,
#                      win32api.MapVirtualKey(win32con.VK_NUMPAD7,3),
#                      win32con.KEYEVENTF_EXTENDEDKEY,
#                      0)  # press
# win32api.Sleep(50)
# win32api.keybd_event(win32con.VK_NUMPAD7,
#                      win32api.MapVirtualKey(win32con.VK_NUMPAD7,3),
#                      win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP,
#                      0)  # r
# import random
#
# print(random.randint(40,60))
#
# from functional import seq
# print(seq(0).find(lambda x:x==1))
# print(seq(None,None))
# from functional import seq
# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.c = "c"
#
# a = A()
# # for k,v in (vars(a).items()):
# #     print(k,v)
# l=seq(vars(a).items()).filter(lambda k:type(k[1]) is int )
# print(l)

# from queue import Queue
# q = Queue(4)
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
# q.put(6)
# print(q.get())
# d  = {1:1}
# print(d.get(2))