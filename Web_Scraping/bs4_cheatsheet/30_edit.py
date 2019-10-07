#----------------------------
# change exisitng tag
#----------------------------
tag.name = "blockquote" # modify tag name
tag['class'] = 'verybold' # modify tag attribute
del tag['class'] # delete attribute
tag.string= 'not too bold' # modify tag contents string
tag.append(" but bolder than usual") # append tag contents

#----------------------------
# insert tag
#----------------------------
new_tag = soup.new_tag("a", href="http://www.example.com")
original_tag.append(new_tag) # create child
new_tag.string = "Link text." # can edit element after creating child

soup.b.string.insert_before(tag)
soup.b.i.insert_after(soup.new_string(" ever "))

#----------------------------
# delete tag
#----------------------------
soup.i.clear() # removes the contents 
i_tag = soup.i.extract() # completely removes a tag from tree and returns the element
soup.i.decompose() # completely removes a tag from tree and discard the tag

#----------------------------
# replace/wrap/unwrap tag
#----------------------------
a_tag.i.replace_with(soup.new_tag("b"))
a_tag.i.replace_with(Beautifulsoup("<b>bold element</b>")) # replace inner html
soup.p.string.wrap(soup.new_tag("b"))
a_tag.i.unwrap()