from category.models import Category

# https://chatgpt.com/s/t_69b9694d9fc08191bee5e7a682ef029b

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

