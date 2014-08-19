# Klout influencer/influencee transforms

There are many things to examine in terms of relationships between Twitter accounts. I very rarely feel the need to consult Klout influencer/influencee connections, but this is something I often do when presented with a new group to examine, so long as they are above board influences of topics of public debate.

Start with a list of notable Twitter accounts and work through either either the influencer or influencee transform in batches of six to eight. Not all accounts are registered for Klout, and despite how simple these transforms are they will mysteriously fail for one or two accounts in each batch which do have Klout profiles. Iteration is key until you have identified all accounts that do NOT have a Klout profile.

It would not be unusual to start with a list of a hundred accounts involved in political debate for a given state and find no overlap in influencees and little overlap in influencers, except for a few big names. A small community may reveal itself in one iteration, but two to four rounds of expanding search are typically needed.

Use color tags liberally in your analysis, especially if mixing influencers and influencees. Tagging initial subjects red, first order influencees orange, second order yellow, and so forth may produce a graph that yields some insight. Counting on degree to ID important accounts will be less effective than you might expect.

#Klout Topics

Klout permits users to select the areas in which they believe they are influential, but this must be supported by conversations on the topic which have been detected passively. When presented with very large groups of Twitter accounts holding multiple interests it is possible to gain insight on overall structure by connecting each user to their respective topics.

#Various Meetup Transforms

Meetup provides clues on real world associations of inviduals. This is a new area for me, so there are just a few small, grubby transforms I've made available. There is a lot more code that is just too raw for public use, but this does seem to be a promising area of research.

#Hurricane Electric BGP

When digging through a lot of ASes I kept finding myself Googling them and ending up on their respective Hurricane Electric pages. This really should be a default included IN the AS entity for Maltego.


#DomainTools

Every domain of interest gets looked up in DomainTools. It was handy to have a transform that drops the URL for each domain into a graph. This code needs to be expanded so it captures not just the URL, but also grabs some of the key content when the URL entity is created. Not everyone has Domain Tools, I frequently find myself transcribing results from the site.