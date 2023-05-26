import re

# RULES:
#.       - Any Character Except New Line
#\d      - Digit (0-9)
#\D      - Not a Digit (0-9)
#\w      - Word Character (a-z, A-Z, 0-9, _)
#\W      - Not a Word Character
#\s      - Whitespace (space, tab, newline)
#\S      - Not Whitespace (space, tab, newline)
#
#\b      - Word Boundary
#\B      - Not a Word Boundary
#^       - Beginning of a String
#$       - End of a String
#
#[]      - Matches Characters in brackets
#[^ ]    - Matches Characters NOT in brackets
#|       - Either Or
#( )     - Group
#
#Quantifiers:
#*       - 0 or More
#+       - 1 or More
#?       - 0 or One
#{3}     - Exact Number
#{3,4}   - Range of Numbers (Minimum, Maximum)

#### Sample Regexs ####
#[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat mat bat pat 
Amrabat is my best friend.

'''
sentence = 'Start a sentence and then bring it to an end'

## -------
#pattern = re.compile(r'[^b]at') # it will match all characters that doesnt start with b and 'at' follows
#pattern2 = re.compile(r'\d{3}.\d{3}.\d{2,4}') # \d{3} means 3 digits follows {2,4} means 2-4 chara follows
#misters = re.compile(r'(Mr|Ms|Mrs)[.]?\s[A-Z]\w*') # it matches: Mr/Ms/Mrs, 0 or 1 dot, whitespace, capital character, word part with 0 or more characters

#matches = misters.finditer(text_to_search)

#for match in matches:
#	print(match.groups()[0])
#

# TRY FOR IMDB PROJECT
from bs4 import BeautifulSoup

text = ''' 
On this one I _have_ to comment... these n**ghty //people make//: $5000 {per sequel!!?} [NONSENSE_!] <h2> #Gr0ßß_boY </h2> also mentioned it... 
Like \\Mad Max II\\", \\"The wild one\\" and /many others/ `dramatize exposition'\x85 show, don't even tell about m*ngolian films, 
long--talk about wanting to go to sleep; @nd reaŁ Łife ˇ˘¤~@ - just sort of plods along\x97no? (So there are no flashy endings). 
[Where will this lead?] -- Big big question.. hmm; why?
<br /><br />~*~Cupid@Grl~*~ 
'''

#text = BeautifulSoup(text, "html.parser").get_text().lower() # it is cool, removes html, better than other approach like br br ...

#text = re.sub(r'[\([{})\]]', '', text) # brackets

#text = re.sub(r'[^\w\s]', '', text, re.UNICODE) # 

# There are also characters like Łß`~ˇ¤
#text = re.sub(r'[^a-z0-9\s]', '', text)

#print(text)



#### -----------------------------------##### 
MLtext = """
['###24293578\n',
 'OBJECTIVE\tTo investigate the efficacy of @ weeks of daily low-dose oral prednisolone in improving pain , mobility , and systemic low-grade inflammation in the short term and whether the effect would be sustained at @ weeks in older adults with moderate to severe knee osteoarthritis ( OA ) .\n',
 'METHODS\tA total of @ patients with primary knee OA were randomized @:@ ; @ received @ mg/day of prednisolone and @ received placebo for @ weeks .\n',
 'METHODS\tOutcome measures included pain reduction and improvement in function scores and systemic inflammation markers .\n',
 'METHODS\tPain was assessed using the visual analog pain scale ( @-@ mm ) .\n',
 'METHODS\tSecondary outcome measures included the Western Ontario and McMaster Universities Osteoarthritis Index scores , patient global assessment ( PGA ) of the severity of knee OA , and @-min walk distance ( @MWD ) .\n',
 'METHODS\tSerum levels of interleukin @ ( IL-@ ) , IL-@ , tumor necrosis factor ( TNF ) - , and high-sensitivity C-reactive protein ( hsCRP ) were measured .\n',
 'RESULTS\tThere was a clinically relevant reduction in the intervention group compared to the placebo group for knee pain , physical function , PGA , and @MWD at @ weeks .\n',
 'RESULTS\tThe mean difference between treatment arms ( @ % CI ) was @ ( @-@ @ ) , p < @ ; @ ( @-@ @ ) , p < @ ; @ ( @-@ @ ) , p < @ ; and @ ( @-@ @ ) , p < @ , respectively .\n',
 'RESULTS\tFurther , there was a clinically relevant reduction in the serum levels of IL-@ , IL-@ , TNF - , and hsCRP at @ weeks in the intervention group when compared to the placebo group .\n',
 'RESULTS\tThese differences remained significant at @ weeks .\n',
 'RESULTS\tThe Outcome Measures in Rheumatology Clinical Trials-Osteoarthritis Research Society International responder rate was @ % in the intervention group and @ % in the placebo group ( p < @ ) .\n',
 'CONCLUSIONS\tLow-dose oral prednisolone had both a short-term and a longer sustained effect resulting in less knee pain , better physical function , and attenuation of systemic inflammation in older patients with knee OA ( ClinicalTrials.gov identifier NCT@ ) .\n',
 '\n',
 '###24854809\n',
 'BACKGROUND\tEmotional eating is associated with overeating and the development of obesity .\n',
 'BACKGROUND\tYet , empirical evidence for individual ( trait ) differences in emotional eating and cognitive mechanisms that contribute to eating during sad mood remain equivocal .\n',
 'OBJECTIVE\tThe aim of this study was to test if attention bias for food moderates the effect of self-reported emotional eating during sad mood ( vs neutral mood ) on actual food intake .\n',
 'OBJECTIVE\tIt was expected that emotional eating is predictive of elevated attention for food and higher food intake after an experimentally induced sad mood and that attentional maintenance on food predicts food intake during a sad versus a neutral mood .\n',
 'METHODS\tParticipants ( N = @ ) were randomly assigned to one of the two experimental mood induction conditions ( sad/neutral ) .\n',
 'METHODS\tAttentional biases for high caloric foods were measured by eye tracking during a visual probe task with pictorial food and neutral stimuli .\n',
 'METHODS\tSelf-reported emotional eating was assessed with the Dutch Eating Behavior Questionnaire ( DEBQ ) and ad libitum food intake was tested by a disguised food offer .\n',
 'RESULTS\tHierarchical multivariate regression modeling showed that self-reported emotional eating did not account for changes in attention allocation for food or food intake in either condition .\n',
 'RESULTS\tYet , attention maintenance on food cues was significantly related to increased intake specifically in the neutral condition , but not in the sad mood condition .\n',
 'CONCLUSIONS\tThe current findings show that self-reported emotional eating ( based on the DEBQ ) might not validly predict who overeats when sad , at least not in a laboratory setting with healthy women .\n',
 'CONCLUSIONS\tResults further suggest that attention maintenance on food relates to eating motivation when in a neutral affective state , and might therefore be a cognitive mechanism contributing to increased food intake in general , but maybe not during sad mood .\n',
 '\n',
 '###25165090\n',
 'BACKGROUND\tAlthough working smoke alarms halve deaths in residential fires , many households do not keep alarms operational .\n',
 'BACKGROUND\tWe tested whether theory-based education increases alarm operability .\n',
 'METHODS\tRandomised multiarm trial , with a single arm randomly selected for use each day , in low-income neighbourhoods in Maryland , USA .\n',
 "METHODS\tIntervention arms : ( @ ) Full Education combining a health belief module with a social-cognitive theory module that provided hands-on practice installing alarm batteries and using the alarm 's hush button ; ( @ ) Hands-on Practice social-cognitive module supplemented by typical fire department education ; ( @ ) Current Norm receiving typical fire department education only .\n",
 'METHODS\tFour hundred and thirty-six homes recruited through churches or by knocking on doors in @-@ .\n',
 'METHODS\tFollow-up visits checked alarm operability in @ homes ( @ % ) @-@ @ years after installation .\n',
 'METHODS\tnumber of homes with working alarms defined as alarms with working batteries or hard-wired and number of working alarms per home .\n',
 'METHODS\tRegressions controlled for alarm status preintervention ; demographics and beliefs about fire risks and alarm effectiveness .\n',
 'RESULTS\tHomes in the Full Education and Practice arms were more likely to have a functioning smoke alarm at follow-up ( OR = @ , @ % CI @ to @ ) and had an average of @ more working alarms per home ( @ % CI @ to @ ) .\n',
 'RESULTS\tWorking alarms per home rose @ % .\n',
 'RESULTS\tFull Education and Practice had similar effectiveness ( p = @ on both outcome measures ) .\n',
 'CONCLUSIONS\tWithout exceeding typical fire department installation time , installers can achieve greater smoke alarm operability .\n',
 'CONCLUSIONS\tHands-on practice is key .\n',
 'CONCLUSIONS\tTwo years after installation , for every three homes that received hands-on practice , one had an additional working alarm .\n',
 'BACKGROUND\thttp://www.clinicaltrials.gov number NCT@ .\n']
"""

# Lists storing foundlings
line_numbers = []
targets = []
texts = []
total_lines = []

# First lets define a pattern:
pattern_line_number = re.compile(r'(###\d{7,9})') # find ###+8 number
pattern_targets = re.compile(r'(BACKGROUND|CONCLUSIONS|RESULTS|METHODS|OBJECTIVE)([\t])?') # find given words
pattern_texts = re.compile(r'([\\\t])(.*)') # finds all text between \t and \n
pattern_total_lines = []

# Then we search it in the text:
matches_line_number = pattern_line_number.finditer(MLtext)
matches_target = pattern_targets.finditer(MLtext)
matches_text = pattern_texts.finditer(MLtext)

# This is what we found:
for match in matches_line_number:
	line_numbers.append(match.groups()[0])
for match in matches_target:
	targets.append(match.groups()[0])
for match in matches_text:
	#print(match.groups()[0])
	texts.append(match.groups()[1])

# print(texts[10:13])




