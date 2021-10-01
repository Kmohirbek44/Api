# import re
#
# txt="This is an example text, this text contains emails, phone numbers "  \
#     "and other sample designed for testing" \
#     "purposes. To use this tool, please type a regular expression in the text-area above."\
#     "When designing regex for emails make sure you cover all possible email types like: info@breatheco.de, " \
#     "dragon23@gmail.com, dragon_ball@yahoo.com.us and also test for bad email formats like ramond=32@skas.com"\
#     "When texting for urls you have samples like this: https://thedomain.com.ve/dir1/dir2.html,"\
#     "ome urls don't have extensions like this http://www.thedomain.net/directory1, " \
#     "maybe you will find some urls with nested subdomains like http://test.www.thedomain.com.ve/directory1"
# lookfor=r"\w+@\w+"
# reg=re.findall(lookfor,txt)
# print(reg)
# a=['Komilov','Mohirbek','4','5','5']
# dictory={
#     'first_name':[],
#     'last_name':a[1],
#
# }
# # a=[]
# for mark in a[2:5]:
#    # a.append(int(mark))
#     dictory['first_name'].append(int(mark))
# a=dict.fromkeys(['a','b'],100)
# # print(dictory.items())
# print(dictory.values())




# from time import sleep
# from rich.console import Console
# from rich import print
# console=Console()
# print('[bold red] hazil[/bold red]')
# tasks=[f"{n} bosqich bajarildi" for n in range(1,8)]
# with console.status('[bold green]bosqich bajarilmoqda[/bold green]') as status:
#     while tasks:
#         task=tasks.pop(0)
#         sleep(1)
#         console.log(f'{task} bajarildi!')
# print('[bold red]Yakunlandi[/bold red]')




#
#
# def return_integer() -> int:
#   return "1"
#
# print(type(return_integer() + "2"))
# nums = list(range(10))
# nums2 = list(range(15))
# nums.extend(nums2)
# print(set(nums))
# a,*b,c=1,2,3,4,5
# print(b)
# a=[1,2,1,2]
# b=set(a)
# a.append(3)
# b=set(a)
# print(b)
# class example:
#
#     def __init__(self, *args, **kwargs):
#         print('a')
# example()
#