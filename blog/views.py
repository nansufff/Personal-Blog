from django.shortcuts import render
from datetime import date
# Create your views here.
all_posts=[
  {
      "slug":"mary-kom",
      "image":"marykom.jpeg",
      "author":"Nandhana Suffin",
      "date":date(2024,7,19),
      "title":"Mary Kom",
      "excerpt":"The other day, while helping my sister with her English homework, I came across the topic of Mary Kom, a figure I've always admired. I first learned about her when I started karate classes in the 11th grade. Inspired by her story, I feel that my first blog should be dedicated to the truly motivating Mary Kom.",
      "content":"""
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
      """
          
  }  ,
  {
    "slug": "abhinav-bindra",
    "image": "abhinavbindra.jpeg",
    "author": "Nandhana Suffin",
    "date": date(2024, 7, 18),
    "title": "Abhinav Bindra",
    "excerpt": "While researching for a project, I stumbled upon the inspiring journey of Abhinav Bindra, India's first individual Olympic gold medalist. His perseverance and dedication towards shooting have always been awe-inspiring, making him a perfect subject for my blog.",
    "content": """
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
    """
},
{
    "slug": "pv-sindhu",
    "image": "pvsindhu.jpeg",
    "author": "Nandhana Suffin",
    "date": date(2024, 7, 17),
    "title": "PV Sindhu",
    "excerpt": "I recently read about PV Sindhu's relentless journey to becoming one of the world's top badminton players. Her story of hard work and triumphs is truly motivational and deserves a place in my blog.",
    "content": """
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
    """
},
{
    "slug": "milkha-singh",
    "image": "milkhasingh.jpeg",
    "author": "Nandhana Suffin",
    "date": date(2024, 7, 16),
    "title": "Milkha Singh",
    "excerpt": "Inspired by the legendary 'Flying Sikh', Milkha Singh, I decided to write about his incredible journey and achievements. His story of overcoming adversity and reaching the pinnacle of success in athletics is a testament to human spirit and determination.",
    "content": """
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sed aliquid distinctio officia repudiandae eum voluptatum nulla, nesciunt dignissimos esse culpa perspiciatis voluptates animi quia natus corporis saepe tenetur maiores accusantium!
    """
}

]


def getdate(post):
    return post['date']
def home(request):
    sorted_posts=sorted(all_posts,key=getdate)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_detail(request,slug):
    identified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request,"blog/post-detail.html",{
        "post":identified_post
    })