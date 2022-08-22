#  package imports main3
import shared.validators

shared.validators.boolean.is_boolean('true')
shared.validators.json.is_json('{}')
shared.validators.numeric.is_numeric(10)
shared.validators.date.is_date('2022-0821')

shared.validators.boolean.is_boolean(True)
print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)  # ***** self *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __annotations__
            # __builtins__
            # __file__
            # __cached__
            # common


print('\n\n***** common *****')
for k in shared.__dict__.keys():
    print(k)  # ***** common *****
            #__name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # validators


print('\n\n***** validators *****')
for k in shared.validators.__dict__.keys():
    print(k)  # ****** validators *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # boolean
            # date
            # json
            # numeric




# print('\n\n***** models *****')
# for k in common.models.__dict__.keys():
#     print(k)  # ***** validators *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # boolean
            # date
            # json
            # numeric


print('\n\n***** numeric *****')#  package imports main
import shared.validators.boolean
import shared.validators.date
import shared.validators.json
import shared.validators.numeric



print('\n\n***** self *****')
for k in dict(globals()).keys():
    print(k)  # ***** self *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __annotations__
            # __builtins__
            # __file__
            # __cached__
            # common


print('\n\n***** common *****')
for k in shared.__dict__.keys():
    print(k)  # ***** common *****
            #__name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # validators


print('\n\n***** validators *****')
for k in shared.validators.__dict__.keys():
    print(k)  # ****** validators *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # boolean
            # date
            # json
            # numeric




# print('\n\n***** models *****')
# for k in common.models.__dict__.keys():
#     print(k)  # ***** validators *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __path__
            # __file__
            # __cached__
            # __builtins__
            # boolean
            # date
            # json
            # numeric


print('\n\n***** numeric *****')
for k in shared.validators.numeric.__dict__.keys():
    print(k)  # ***** numeric *****
            # __name__
            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __file__
            # __cached__
            # __builtins__
            # is_integer
            # is_numeric
            # numeric_helper_1
            # numeric_helper_2

            # __doc__
            # __package__
            # __loader__
            # __spec__
            # __file__
            # __cached__
            # __builtins__
            # is_integer
            # is_numeric
            # numeric_helper_1
            # numeric_helper_2
