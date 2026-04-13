import pygame
import math
import random
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button


def draw_ellipse_angle(surface, rad_x, rad_y, angle, width=2,color="red",radius=5):
    target_rect = pygame.Rect((-rad_x + screen.get_width() / 2 - radius - 1,-rad_y + screen.get_height() / 2 - radius - 1,rad_x*2 + radius + 1 ,rad_y*2 + radius + 1))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, (-(angle -g_angle*t)))
    transformed_surf = pygame.transform.scale(rotated_surf, (rotated_surf.get_width(),rotated_surf.get_height()*td))
    surface.blit(transformed_surf, transformed_surf.get_rect(center = target_rect.center))

def draw_stars(surface,num, ecc, d_rot, rad, dr,color="white",radius=5):
    #target_rect = pygame.Rect(1,1,surface.get_width(),surface.get_height)
    #pygame.draw.circle(surface, color, ((surface.get_width()/2),(surface.get_height()/2)), radius*5)
    for i in range(num):
        a = rad+ i*dr #radius in x and y
        b = math.sqrt((ecc*ecc + 1)*a*a)
        rel_angle = i*d_rot
        speed = rad / a
        random.seed(i)
        w = random.random()
        sdot_pos = pygame.Vector2(a * math.cos(-t*speed + 2*w*math.pi),b * math.sin(-t*speed + 2*w*math.pi))
        rot_sdot_pos = sdot_pos.rotate((rel_angle-g_angle*t))
        #print(rot_sdot_pos.y /surface.get_height())
        #star_temp = int((255-((1-td)*(100*((-2*rot_sdot_pos.y /surface.get_height()) +.5)))))
        star_temp = 255
        #if star_temp > 255: star_temp = 255
        #if star_temp < 0: star_temp = 0
       # rot_sdot_pos.x *=int(abs((1-((1-td)*(.01*((-2*rot_sdot_pos.y /surface.get_height())))))))
        rot_sdot_pos.x += surface.get_width()/2

        rot_sdot_pos.y *= td
        rot_sdot_pos.y += (surface.get_height()/2)
        star_color = pygame.Color(star_temp,star_temp,star_temp)
        pygame.draw.circle(surface, star_color, rot_sdot_pos, radius)

def gen_orbits(surface, num, ecc, d_rot, rad, dr): #number of orbits, eccentricity, delta rotation, first radius of ellipse, delta radius
    q = num / 20
    for i in range(20):
        a = rad+ q*i*dr #radius in x and y
        b = math.sqrt((ecc*ecc + 1)*a*a)
        rel_angle = q*i*d_rot
        speed = rad / a
        random.seed(i)
        if show_orbits == True : draw_ellipse_angle(surface, a,b, rel_angle)
    if show_stars == True : draw_stars(surface,num,ecc,d_rot,rad,dr)
                  
    
def dopause():
    global pause
    if  pause == True:
        pause=False
    else:
        pause = True
    return()
def dostars():
    global show_stars
    if  show_stars == True:
        show_stars=False
    else:
        show_stars = True
    return()
    return()
def doorbitals():
    global show_orbits
    if  show_orbits == True:
        show_orbits=False
    else:
        show_orbits = True
    return()

# pygame setup
pygame.init()
pygame.display.set_caption("ArmSim 2.1")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
t = 0
g_angle = 4 #galaxy rotation 
n_stars = 100
show_orbits = True
show_stars = True
pause = False
e = .9
td = 1 #psuedo3difyer
oda = .4 #delta angle between orbits
r_interior = 50
dr = .1
font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render("Aestelle Dondero, OWU '27", True, pygame.Color('#4E1535'))

#button colors
pc = (0, 255, 0)

n_stars_slider = Slider(screen, 130, 10, 150, 20, min=1, max=2000, step=1,handleColour=(255,255,255))
n_stars_out = TextBox(screen, 10, 10, 110, 30, fontSize=15)
n_stars_out.disable()  # Act as label instead of textbox

e_slider = Slider(screen, 130, 50, 150, 20, min=0, max=1, step=.001,handleColour=(255,255,255),initial =.9)
e_out = TextBox(screen, 10, 50, 110, 30, fontSize=15)
e_out.disable()  # Act as label instead of textbox

oda_slider = Slider(screen, 130, 100, 150, 20, min=0, max=3, step=.001,handleColour=(255,255,255),initial =.4)
oda_out = TextBox(screen, 10, 100, 110, 30, fontSize=15)
oda_out.disable()  # Act as label instead of textbox

dr_slider = Slider(screen, 130, 150, 150, 20, min=0, max=1, step=.001,handleColour=(255,255,255),initial =.1)
dr_out = TextBox(screen, 10, 150, 110, 30, fontSize=15)
dr_out.disable()  # Act as label instead of textbox

gr_slider = Slider(screen, 130, 200, 150, 20, min=0, max=20, step=.001,handleColour=(255,255,255),initial =4)
gr_out = TextBox(screen, 10, 200, 110, 30, fontSize=15)
gr_out.disable()  # Act as label instead of textbox

Pbutton = Button(screen, 10,250,70,30,text="Pause",fontSize=15,inactiveColour=(0,255,0),pressedColour=(255,0,0),radius=20,onClick=lambda:dopause()) 
Sbutton = Button(screen, 90,250,70,30,text="Stars?",fontSize=15,inactiveColour=(0,255,0),pressedColour=(255,0,0),radius=20,onClick=lambda:dostars()) 
Obutton = Button(screen, 170,250,80,30,text="Orbitals?",fontSize=15,inactiveColour=(0,255,0),pressedColour=(255,0,0),radius=20,onClick=lambda:doorbitals())

td_slider = Slider(screen, 130, 300, 150, 20, min=0, max=1, step=.001,handleColour=(255,255,255),initial = 1)
td_out = TextBox(screen, 10, 300, 110, 30, fontSize=15)
td_out.disable()  # Act as label instead of textbox

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen_rect = pygame.Rect(1,1,screen.get_width(),screen.get_height())
    sub_screen = pygame.Surface((1280,720), pygame.SRCALPHA)
    gen_orbits(sub_screen,n_stars,e,oda,50,dr)
    screen.blit(sub_screen, sub_screen.get_rect(center = screen_rect.center))
    # flip() the display to put your work on screen

    n_stars = n_stars_slider.getValue()
    n_stars_out.setText("N_Stars: "+ str(n_stars))

    e = e_slider.getValue()
    e_out.setText("e = "+ str(e))

    oda = oda_slider.getValue()
    oda_out.setText("d\u03B8/dr ="+ str(oda))

    dr = dr_slider.getValue()
    dr_out.setText("dr ="+ str(dr))

    g_angle = gr_slider.getValue()
    gr_out.setText("d\u03B8/dt ="+ str(g_angle))

    td = td_slider.getValue()
    td_out.setText("\u03D5 ="+ str(td))

    screen.blit(text,(1080,700))
    
    pygame_widgets.update(events)
    pygame.display.update()

    pygame.display.flip()    
    if pause == False:
        t += dt
    else: t = t 
    dt = clock.tick(60) / 1000


pygame.quit()
