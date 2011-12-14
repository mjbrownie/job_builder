leadins = """There is an opening for a
    We need a
    The company needs a
    Our industry needs a
    We are looking to fill a critical shortage in the position of
    There is a dire need of a
    Within our organisation there is a
    There is an opening for a
    Our client desires a
    There is an opening for a
    Can you be a
    We have an opening for a"""
# List of LEADINs to buy time.

jobs = """ faithful  party patron
    fail safe prodiver of a service
    dilligent and worthy vestige
    honourable mentor
    bald headed forty something
    architect of considerable experience
    desirable candidate of nobile origins
    friendly, sociable  Magda Subanski type
    philosopical, possibly creepy general practitioner
    hot chick
    muscle bound hero head
    suit
    aggressive expansionist hot head type
    motivated individual
    independent practitioner
    short ass
    monotonous toned troglodyte"""
# List of SUBJECTs chosen for maximum professorial macho.

verbs = """to account for our massive
    to stand casually by a
    to spruik the
    with an astute understanding of
    with a persistant passion for managing a
    that will valiantly stand by our
    to clean a
    to help justify our
    to bless our
    to trilateralize our
    to manage our
    to supervise our
    to handle our
    to provide comfort for our
    thad can be unaffected by the merciless panderings of a"""
#List of VERBs chosen for autorecursive obfuscation.

companies = """dodgy investment company.
    tractor pulling contest.
    Maldovan hedge fund.
    Pie Floter van.
    Gothic Cathedral.
    Gymnaseum.
    Surface to air missile factory.
    newspaper.
    snarky art nouveau catalogue.
    porpoise farm.
    Fried chicken restaurant.
    Law firm.
    Horse Knackery.
    Processed meat factory.
    music store.
    Pleasure dome.
    Salvation army band."""
# List of OBJECTs selected for profound sententiousness.

q_leadin = """Do you have the capacity to
Will you be able to 
Are you able to
Can you
Moreover, will you
Would you
Please, Can you
Will you"""

q_adverb = """diligently,
proudly,
fluidly,
dispassionately,
passionately
soundly
conspiratorially
confidentially
abusively
competently
precisely
convincingly
surreptitiously
gladly"""

q_verb = """preserve our
manage our
sort out our
motivate our
dish out our
service our
smear oil and tar over our
gesticulate madly over our
burn our
organise our
defeat our
"""
q_object="""accounts,
chickens,
Soviet era helicopters,
technical infrastructure,
hot headed upper management,
field of daisies,
erotic poem collection,
corporate image,
plastic exterior,
stocks,
monster truck collection,
bosses daughter,
mystical idol,
high rating cable television show
pain in the arse customers
financial accounts
mass of uncatalogued text books
horny teenage female crew
dog
toilets
reputation
debts,
chocolate factory,
battery hen floor if incompetent journalists,
geostationary orbiting satellite weapons platform,
ethnically partitioned small European economy,"""

q_post_ojbect="""with a sense of
without a sense of
despite the need for
with a case for
as a matter of
"""

q_descriptive="""urgency?
basic competence?
guilt?
compassion?
cheeky swagger?
cleanliness?
self belief?
motivation?
clinical perfection?
collusion?
ecstatic rejoicing?
joint disregard for the common good?
the social contract?
voyeurism?
yearning?"""


t_adject = """Chief Operations
Technical
Statistical
Belligerent
Clinical
Sentient
Systems
Professional
Smiling
Co operative
Co Adaptive
Green
Plankton
Unscrupulous
Mildly Ironic
Psychotic
Psychic
Smug
Evaluative
Vehicle
Boat
Tropical
Laser
Underwater
Evil
Kick ass
Progressive
Motivated
Bloated
Right Wing
Trans Atlantic
Theatrical
Little
Puny
Heroic
Paid
Nude
Post Modern
Young
Junior"""

t_noun= """Developer
Provider
Manager
Head Kicker
Number Cruncher
Cleaner
Decision Maker
Chest Beater
Driver
Guitarist
Television Zombie
Spleen Splitter
Diplomat
Lumberjack
Planner
Plastic Surgeon
Psychiatrist
Surgeon
Thrill Seeker
Television Presenter
Whittler
Executioner
Housewife
Clerk
Teacher
Physicist
Comedian
Chiropractor
Gold Digger
Commando
Pilot
Pall Bearer
President
Architect
Skipper
Writer
Author
Cop
Politician
Dictator
Linguist
Specialist
Thug
Adviser
Sycophant
Coroner
Officer
Upstart
Script Kiddie
God
Overlord
Gambler
Drunk"""


cat_adjective = """Retail
Central
Aloof
Robotic
Medical
Psychiatric
Animal
Private
Collaborative"""

cat_noun = """Therapy
Planning
Intervention
Military
Government
Industry
Retail
Beauty"""



import textwrap, random
from itertools import chain, islice, izip

def intro_sentence(times=1, line_length=72, jobs=jobs):
    parts = []
    for part in (leadins, jobs, verbs, companies):
        phraselist = map(str.strip, part.splitlines())
        random.shuffle(phraselist)
        parts.append(phraselist)
    output = chain(*islice(izip(*parts), 0, times))
    return textwrap.fill(' '.join(output), line_length)

def question(times=1, line_length=72):
    parts = []
    for part in (q_leadin, q_verb, q_object, q_post_ojbect, q_descriptive):
        phraselist = map(str.strip, part.splitlines())
        random.shuffle(phraselist)
        parts.append(phraselist)
    output = chain(*islice(izip(*parts), 0, times))
    return textwrap.fill(' '.join(output), line_length)

def job_title(times=1, line_length=72):
    parts = []
    for part in (t_adject, t_noun):
        phraselist = map(str.strip, part.splitlines())
        random.shuffle(phraselist)
        parts.append(phraselist)
    output = chain(*islice(izip(*parts), 0, times))
    return textwrap.fill(' '.join(output), line_length)

def category(times=1, line_length=80):
    parts = []
    for part in (cat_adjective, cat_noun):
        phraselist = map(str.strip, part.splitlines())
        random.shuffle(phraselist)
        parts.append(phraselist)
    output = chain(*islice(izip(*parts), 0, times))
    return textwrap.fill(' '.join(output), line_length)


if __name__ == '__main__':
    title = job_title()
    print
    print title
    print
    print intro_sentence(jobs=title)
    print
    print question()
    print question()
    print question()
    print
    print "If you are interested, Please Apply"
    print


