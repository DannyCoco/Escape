import sys
import time

#Time Delay Effect
a=1
b=0.01
c=0.08

# Title Screen
def startGame():
    print()
    print()
    print("      ######################")
    print("      #                    #")
    print("      #   Time Unraveled   #")
    print("      #                    #")
    print("      ######################")
    print()
    time.sleep(a)

    user_input = input("Would you like to start the game? (Y/N): ")
    if user_input.lower() != 'y':
        print('Game not started, maybe next time!')
        startGame()
    else:
        return

def intro():
    print()
    plot = '''You awaken... surrounded by the debris of the collapsed surface floor above you, you assume you fell from.
Sirens blaring as you doze in and out of conciousness, you realize you fell into a laboratory. You look
around, an AR with an empty clip and a briefcase. You wonder how you got here, but as you begin to think, 
footsteps in the distance become louder and louder. They're coming.'''
    for char in plot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print()
    while(True):
        time.sleep(a)
        print()
        print('1. Head towards the exit signs, away from the footsteps.')
        print('2. Go towards the sound of the footsteps.')
        print('3. Do nothing.')
        first_choice = input()
        if first_choice not in ('1', '2', '3'):
            pass
        else:
            if first_choice == '1':
                path = 1
                return path
            elif first_choice == '2':
                path = 2
                return path
            elif first_choice == '3':
                path = 3
                return path

def path1( ):
    print()
    plot = '''As you sprint toward the dimly lit exit sign, adrenaline pumps through your veins. The twisting corridors 
lead you to a ladder—an escape route. You climb, pushing open the hatch, and emerge into the star-filled night sky. The 
compound behind you is engulfed in flames, gunshots echoing in the distance. You’ve left your allies behind, but at least 
you’re safe… for now. The desert stretches before you, its vastness both comforting and daunting. The AR in your hand feels 
heavier now, its empty clip a reminder of the danger you’ve narrowly escaped. You wonder about the lab—the secrets buried 
within its ruins. Who were your allies? Why did they betray you? The night wind whispers ancient secrets, and you clutch 
the briefcase tighter. Dr. Elana’s words echo in your mind: “The coordinates to a better timeline.” But what does that mean? 
Is there really a place where you can rewrite your fate? You glance back at the flames, wondering if anyone survived. 
The footsteps fade, replaced by the haunting silence of the desert. The stars above seem to hold answers, distant and unreachable. 
You take a deep breath, ready to forge your path—one that leads beyond the wreckage, beyond the gunfire, and into the unknown.'''
    for char in plot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print()
    while(True):
        time.sleep(a)
        print()
        print('1. Follow the coordinates.')
        print('2. Wander around the desert aimlessly.')
        second_choice = input()
        if second_choice not in ('1', '2'):
            pass
        else:
            if second_choice == '1':
                second_path = 1
                return second_path
            elif second_choice == '2':
                second_path = 2
                return second_path

def path2():
    print()
    plot = '''As you approach the sound of the footsteps, your heart races. The dimly lit corridor reveals a
figure—a woman in a lab coat, her eyes wide with fear. It’s Dr. Elana, the lab’s head doctor. She gasps when 
she sees you. “Quick!” she whispers urgently. “We don’t have much time. They’re after the time-travel device—the
one you fell through. It’s a prototype, and they want it back.” You glance at the AR in your hand, realizing its significance. 
Dr. Elana grabs your arm, pulling you toward an unmarked door. “We need to hide,” she says. “There’s a secret chamber below 
the lab. Follow me.” Together, you descend a narrow staircase, the air growing colder. The walls are lined with ancient symbols,
and the floor vibrates faintly. Dr. Elana explains that the device isn’t just a time-travel tool—it’s a gateway to alternate 
realities. Whoever controls it could reshape history. As you reach the hidden chamber, she mentions the briefcase. 
“This contains the key,” she says. “The coordinates to a safer timeline. You must protect it at all costs.
Dr. Elana leads you deeper into the chamber. You stand in the secret chamber, the symbols pulsing around you. 
Dr. Elana eyes you, her lab coat billowing. She points to two doors: “The left one!”'''
    for char in plot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    print()
    while(True):
        time.sleep(a)
        print()
        print('1. Door on the left.')
        print('2. Door on the right.')
        second_choice = input()
        if second_choice not in ('1', '2'):
            pass
        else:
            if second_choice == '1':
                second_path = 1
                return second_path
            elif second_choice == '2':
                second_path = 2
                return second_path

def path3():
    print()
    plot ='''Frozen by fear, you remain still. The footsteps draw closer until a masked figure emerges from the shadows. 
They raise a gun, and time seems to slow. You think of your allies, the ones who trusted you, and the betrayal weighs heavy.
The gunshot echoes through the corridor, and darkness envelops you. Your last thought is of the lab, the debris, and the unanswered 
questions. Who pushed you? Why? And what secrets lie buried beneath the rubble? In another reality, perhaps you made a different
choice. But here, in this fractured timeline, your journey ends abruptly. The footsteps fade, and the world slips away.'''
    for char in plot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    return 'bad'

def path1_1():
    print()
    plot = '''The desert sun beats down mercilessly as you stumble across the arid landscape. The coordinates lead you to a crumbling
ruin—an abandoned lab. Dr. Elana confronts you, furious you left her to die. She demands the briefcase, her eyes cold. You hesitate. 
She pulls a gun, and you realize too late that she orchestrated the entire collapse. The lab was a trap. She shoots you, leaving you 
bleeding in the sand. As your vision fades, you glimpse her reach for the briefcase as you being fading away. She heads towards the dirction you came from, leaving you to die. 
The desert swallows your last breath, and the secrets of the lab remain lost forever.'''
    for char in plot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    return 'bad'

def path1_2():
    print()
    plot = '''You trek through the desert, guided by the stars lighting up the night sky. As dawn approaches, you discover
an ancient cave hidden among the dunes. Inside, you find the true location to the time-travel portal—the gateway to a safer timeline. 
With hope in your heart, you step through, leaving behind the chaos of your world. You emerge in a lush forest, birds singing, and 
sunlight filtering through leaves. The air smells different here—a promise of peace. You’ve rewritten your fate, and the secrets of
the lab remain buried. You’re safe, and perhaps, so is humanity.'''
    for char in plot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    return 'good'

def path2_1():
    print()
    plot = '''You take a deep breath and step into the shimmering portal. The world shifts around you—a kaleidoscope of colors and sensations.
When you open your eyes, you’re standing in a bustling city square. People laugh, children play, and the air smells of blooming flowers. 
This is the safer timeline—the reality you’ve longed for. Dr. Elana appears beside you, her expression softer now. “We did it,” she whispers. 
“We’ve rewritten history.” You become a guardian of this new world, the AR a relic of the past. The empty clip? A symbol of hope. You’ve found 
your place in this reality, and the lab’s secrets remain buried forever.'''
    for char in plot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    return 'good'

def path2_2():
    print()
    plot = '''Curiosity tugs at you. You ignore Dr. Elana’s warnings and delve into the hidden archives. Dusty scrolls reveal dark rituals, forbidden 
incantations, and glimpses of alternate realities. You decipher a spell—the ultimate power to reshape time. Dr. Elana watches, horror in her eyes. You 
recite the incantation, and reality fractures. The lab collapses, screams echoing. You become a god of chaos, rewriting history with reckless abandon. 
But the cost is high—the world crumbles, and you’re left floating in a void of your own making. The briefcase slips from your grasp, its secrets lost 
forever. You’ve become the betrayer, and the footsteps fade into oblivion.'''
    for char in plot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(b)
    return 'bad'

def ending(end):
    print()
    time.sleep(a)
    print(end.upper() + ' ENDING.')
    time.sleep(a)
    print('GAME OVER.')