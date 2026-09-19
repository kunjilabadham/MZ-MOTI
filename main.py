from manim import *
import os

class ShrinithiInfraPromo(Scene):
    def construct(self):
        # Branding
        title = Text("Shrinithi Infra", font_size=72, color=BLUE)
        subtitle = Text("Building Your Dreams", font_size=36, color=WHITE)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1.5)
        
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Displaying Accomplishments
        accomplishments = [
            "assets/signature-work-1.webp",
            "assets/signature-work-2.webp",
            "assets/signature-work-3.webp",
            "assets/signature-work-4.webp",
            "assets/signature-work-5.webp",
            "assets/signature-work-6.webp",
        ]
        
        # Let's show them one by one with a simple fade
        for img_path in accomplishments:
            if os.path.exists(img_path):
                img = ImageMobject(img_path)
                # scale to fit nicely in 1080p (height is 8 by default in manim units)
                img.height = 5
                
                caption = Text("Signature Work", font_size=32)
                caption.next_to(img, DOWN)
                
                self.play(FadeIn(img), FadeIn(caption), run_time=0.8)
                self.wait(1.5)
                self.play(FadeOut(img), FadeOut(caption), run_time=0.5)
        
        # Contact Info
        contact_title = Text("Contact Us", font_size=60, color=BLUE)
        contact_num = Text("+91 XXXXX XXXXX", font_size=48, color=GREEN) # Placeholder, update as needed
        contact_num.next_to(contact_title, DOWN)
        
        self.play(Write(contact_title))
        self.play(FadeIn(contact_num))
        self.wait(3)
        self.play(FadeOut(contact_title), FadeOut(contact_num))
