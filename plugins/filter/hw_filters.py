#########################################
# hello_world collection's filter plugins
#########################################

# hw_to_upper filter
# converts all lowercase characters in a string into uppercase characters
def filter_to_upper(in_string):
    return in_string.upper()


# filter module
class FilterModule(object):
    def filters(self):
        return {
                'hw_to_upper': filter_to_upper
        }
