# Unofficial-Anchor-API
An unofficial API for Anchor.fm to extract essential details about a podcast series

Parses through the RSS feed of the podcast and returns details in json in a well formatted manner

#### Usage

```
Request URL : https://anchorapi.herokuapp.com/path/<rss_feed_url>
```

#### Request

```
Request URL: https://anchorapi.herokuapp.com/path/https://anchor.fm/s/3c55a5f0/podcast/rss
Request Method:GET
Status Code:200 OK

```


##### Response

```

[
  {
    "date_of_publishing": "20 Oct 2020",
    "description": "Presenting DSC Afterhours, a podcast show hosted by Developer Student Clubs VIT. DSC Afterhours is a new series of podcast discussions by the members of DSC VIT to talk about their journey in tech, learn new things, have fun and impart knowledge in the process. In each episode, our team of caffeine-addicted developers and gradient-loving designers sit down, talk, and have discussions on various technical and fun topics. Check out each episode stream live on our YouTube Channel.",
    "episode": 0,
    "iframelink": "https://anchor.fm/dsc-vit/embed/episodes/Introducing-DSC-Afterhours-elalj4",
    "title": "Introducing DSC Afterhours"
  },
  {
    "date_of_publishing": "20 Oct 2020",
    "description": "With the Hacktoberfest coming up, the DSC Team talks about the role of open-Source in tech and how it will shape the future of software. In this episode, we have some great developers from our team who love the idea of open-source software and will guide you through the process of submitting Pull-Requests to complete the Hacktoberfest Challenge. &nbsp; Hacktoberfest Event Page: https://hacktoberfest.digitalocean.com/ Learn how to make a Pull-Request: http://bit.ly/PRsHowTo",
    "episode": 1,
    "iframelink": "https://anchor.fm/dsc-vit/embed/episodes/Hacktoberfest--Open-Source-Stories-elb8ri",
    "title": "Hacktoberfest & Open-Source Stories"
  },
  {
    "date_of_publishing": "23 Oct 2020",
    "description": "Hackathons are a place where ideas turn into realities for developers. Many devs from all fields of development agree that a hackathon was the first step to something big and life-changing in their lives. Hackathons are also a place for developers to come out of their comfort zones in order to learn, network, and interact with other people. A lot of modern-day startups and major companies were born from a band of innovators coming together and creating something new in a hackathon!&nbsp; In the very spirit of fostering developer communities, the DSC VIT team has conducted multiple hackathons over the past few years and has participated in plenty more. Our last hack, WomenTechies 2020, left our participants with a fulfilling new experience that they were excited to share with their peers as well as sparked their flame to develop and contribute more to the world around them. &nbsp;In this episode of DSC Afterhours, we have guests from Developer Student Clubs LPU, to share hackathon stories and together we will discuss projects that we have made during caffeine-fuelled nights. You can read more about our flagship hackathon, DevJams here: https://medium.com/gdg-vit/devjams-no...",
    "episode": 2,
    "iframelink": "https://anchor.fm/dsc-vit/embed/episodes/Hackathons-and-Over-Night-Projects-elg361",
    "title": "Hackathons and Over Night Projects"
  },
  {
    "date_of_publishing": "12 Nov 2020",
    "description": "A scholarship is not only a financial benefit but also a matter of pride and sense of achievement for any student in their college journey. DSC Afterhours is a new series of podcast discussions by the members of DSC VIT to talk about their journey in tech, learn new things, have fun and impart knowledge in the process. In Episode 3 of DSC-Afterhours, we have the DSC-VIT team along with our friends from DSC-NSEC to talk about the importance and share their journey of getting scholarships from renowned programs across the globe. WTM Website: www.womentechmakers.com",
    "episode": 3,
    "iframelink": "https://anchor.fm/dsc-vit/embed/episodes/Student-Scholarships-and-Fellowships-emd835",
    "title": "Student Scholarships and Fellowships"
  },
  {
    "date_of_publishing": "02 Dec 2020",
    "description": "In Episode 4 of DSC-Afterhours, we have the DSC-VIT team along with a Product Designer at Paytm Insider to talk about the various aspects of design and how can one make a career in design. Additionally, they will also be talking about how one can harness inspiration from Instagram, Dribbble or Behance to kickstart their design journey.&nbsp; DSC Afterhours is a new series of podcast discussions by the members of Developer Student Clubs to talk about their journey in tech, learn new things, have fun and impart knowledge in the process. The Bezier Game: https://bezier.method.ac/",
    "episode": 4,
    "iframelink": "https://anchor.fm/dsc-vit/embed/episodes/Design-Journey-and-Challenges-en8r83",
    "title": "Design Journey and Challenges"
  }
]

```
