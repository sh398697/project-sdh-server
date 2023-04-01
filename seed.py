#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Friendship, Post

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///data.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.query(User).delete()
    session.query(Friendship).delete()
    session.query(Post).delete()

    scott_henry = User(
        email="scotthenry1@gmail.com",
        fname="Scott",
        lname="Henry",
        location="Maplewood, NJ",
        image="https://roost.nbcuni.com/bin/viewasset.html/content/dam/Peacock/Landing-Pages/2-0-design/the-office/cast-the-office-michael-scott.jpg/_jcr_content/renditions/original.JPEG"
    )
    
    austin_henry = User(
        email="austin",
        fname="Austin",
        lname="Henry",
        location="Maplewood, NJ",
        image="https://cdn.geekwire.com/wp-content/uploads/2021/06/stephcurry.jpg"
    )
    
    dylan_henry = User(
        email="dylan",
        fname="Dylan",
        lname="Henry",
        location="Maplewood, NJ",
        image="https://media.gettyimages.com/id/1204945230/photo/aaron-judge-of-the-new-york-yankees-poses-during-photo-day-on-thursday-february-20-2020-at.jpg?s=612x612&w=gi&k=20&c=ZYT9TWzvE_Pd1JRGOf1ClyZ7tNRMCuiXo-gzSU4MnfE="
    )

    scott_austin_friendship = Friendship(
        friend1_id=1,
        friend2_id=2,
        status="confirmed"
    )
    
    scott_dylan_friendship = Friendship(
        friend1_id=1,
        friend2_id=3,
        status="confirmed"
    )
    
    austin_dylan_friendship = Friendship(
        friend1_id=2,
        friend2_id=3,
        status="confirmed"
    )
    
    post_1 = Post(
        text="Hello World!",
        author_id=1,
        recipient_id=1,
    )

    post_2 = Post(
        text="Hi Austin!",
        author_id=1,
        recipient_id=2,
    )

    post_3 = Post(
        text="Hi Dylan!",
        author_id=1,
        recipient_id=3,
    )

    post_4 = Post(
        text="Hi Bro!",
        author_id=2,
        recipient_id=3,
    )

    post_5 = Post(
        text="Hi Bro!",
        author_id=3,
        recipient_id=2,
    )

    post_6 = Post(
        text="Hi Dad!",
        author_id=2,
        recipient_id=1,
    )

    post_7 = Post(
        text="Hi Dad!",
        author_id=3,
        recipient_id=1,
    )

    session.bulk_save_objects([scott_henry, austin_henry, dylan_henry, scott_austin_friendship, scott_dylan_friendship, austin_dylan_friendship, post_1, post_2, post_3, post_4, post_5, post_6, post_7])
    session.commit()
    session.close()
