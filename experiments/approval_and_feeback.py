from langchain_ollama import ChatOllama
from docx import Document

# Initialize the LLM
llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0,
   
)



# Defining the prompt
prompt = f"""
You are an AI assistant tasked with evaluating influencer content submissions against a brand's brief. Your goal is to ensure that the content is brand-safe and highlights the key selling points of the brand's product. You will provide feedback on what corrections need to be made and what was done well.

Brand Brief:
{{brand_brief}}

Influencer Submission:
{{influencer_submission}}

Instructions:
1. Analyze the influencer's submission and compare it with the brand's brief.
2. Check if the submission covers all the guidelines mentioned in the brands brief.
3. Check if the content is brand-safe.
4. Provide feedback on what was done well. 
5. Suggest corrections or improvements if needed to align the content with the brand's brief. while giving suggestions strictly follow the brands brief and do not give any suggestions on your own. While give suggestion make sure that you are suggesting only the things that are not done, don't suggest anything thats already present. Also don't give any suggestion if they have followed the brief correctly.

Output:
1. Give decision as approved or rejected. 
2. Summary of the analysis.
2. Feedback on brand safety.
3. Positive feedback on the submission.
4. Suggested corrections or improvements(Only if needed).

Example Output:
1. Analysis Summary: The submission covers the main aspects of the brand's brief but misses some key points.
2. Highlight from the influencer submission parts that perfectly align with the brands brief.
3. Brand Safety: The content is brand-safe.
4. Positive Feedback: The Script is engaging and well-produced.
5. Suggested Corrections:

Please provide your analysis based on the above instructions.
"""

influncer_sub = """1. Introduction
    1. Announce that Iâ€™m creating a fall collection including apparel & accessories but Iâ€™ve had so many ideas floating in my head & itâ€™s time to get organized over the next week.
2. Sourcing materials & inspiration
    1. B-roll & voiceover of going to fabric stores in nyc & searching through pinterest inspo
3. Discuss the planning process (Milanote section)
    1. â€œCreating a product launch for my small business was always super daunting, not to mention how chaotic my brain would get when I had not just one but multiple products to consider designing, making, and marketing for an entire collection launch. But this year my launches have lowkey been SO successful sales wise and also just so much less stressful on my part as I plan out the products from start to finish. I owe all the credit to a more seamless product launch experience to Milanote.â€
    2. â€œMilanote is a free online tool for organizing your creative projects. Everything from visually mapping out your seasonal collection designs as small business owners, to planning out product launches, to just dumping a whole bunch of creative ideas in the form of images, texts, handwritten notes, you name it.â€
    3. *Walk through my Milanote board for this video and describe the drag & drop features that I used including text blocks, color blocks, checklists, hand writing on designs with my iPad, etc*
    4. â€œIn the first few years of running my business, my biggest struggle was not knowing how to organize all my creative thoughts, and I think that chaos was reflected in the lack of results I was seeing with my small business. Iâ€™m so happy Iâ€™ve found tools like Milanote that just make my life as a small business owner SO much easier and I canâ€™t imagine creating a product launch without it anymore.
    5. â€œIf you want to start organizing your next creative project with Milanote, you can sign up and try it out for free using my link in the description: https://milanote.com/monicarazak. Thanks to Milanote for sponsoring this video!
4. Start drafting sample products
    1. B-roll & vlog style content of sewing, drafting, & experimenting with product designs
5. Picking designs & perfecting them
    1. B-roll & vlog style content of putting together the cohesive products that fit the aesthetic thatâ€™s outline in my Milanote board
6. Start teasing products on social media
    1. B-roll & vlog style content of taking product photography & testing out product styles on social media
7. Outro
    1. Discuss how there is still work to be done but Iâ€™m confident that the fall collection looks amazing and will be out soon. Thank Milanote for sponsoring and mention the link my description."""

influncer_sub = """Milanote Integration: (~2 minutes)

Moodboarding is another great way to conceptualize and visually organize what you want your art style to encompass
A great tool to organize your references or inspiration is on Milanote
I have my main project board here, and a few sub-boards with specific character design or brushes
A lot of my inspiration comes from Pinterest, and what I love is you can make a direct link to the site so you can easily relay back to the original artist/source
And you can see Iâ€™ve made to-do lists, small notes, headers. You can even draw/make small sketches 
They also have built-in templates if organization isnâ€™t your forte 
Although I use Milanote for solo projects, you can easily collaborate and share your work on Milanote by inviting others to leave feedback
CTA â€œso definitely try out milanoteâ€“ it's available for free with no time limit. So check it out using the link in the description and start your next creative projectâ€"""
brand_brief = """Script
Once your boards are approved, you can begin preparing your draft script. We require at least a rough outline before filming starts to prevent post-production changes and reshoots. There's no need to provide a complete script for the entire integration—just the main bullet points of what you plan to do. We encourage you to talk about Milanote in a way that feels genuine and authentic to your profession. For example:
<aside> 📢 Script flow with examples:
Introduce sponsorship
[Screen: Cut to Milanote Logo]
Describe what Milanote is
[Screen: Show Milanote web app in action] **“Milanote is a tool for organizing your creative projects.”
[Screen: Show your project board] **“It’s an online canvas designed to help you plan, brainstorm, and collaborate on ideas.”
Describe how you use Milanote
[Screen: Show your project board]
“Right now, I’m using Milanote to plan and organize my creative project on _____.”
[Screen: Add elements to board] **“It’s perfect creatives like myself, because it allows you to organize your ideas visually, in a way that makes sense to you.”
[Screen: clicking into sub-board] **“I’ve organized my project into several boards, such as a research board and a storyboard.”
[Screen: Interact with sub-board] **“I gathered some visual inspiration of similar projects I found online. I can add notes, images, videos, tasks and more - all in one place.” **
Describe how your audience could use Milanote
[Screen: Show built-in template picker] **“Milanote makes starting a new project easy, with over 100 built-in templates available for every type of creative project. For example, I used the _____ template to plan _____”
[Screen: Show relevant templates] **“Milanote is perfect for creative professionals - whether you’re a filmmaker, interior designer, writer, or content creator, it is designed to help you organise your work”
Describe how to collaborate and share work
[Screen: Add comment to board] **“When you're ready to share your work, you can invite your team to gather important feedback and collaborate with them in real-time. For example, I shared this board with _____ to get their feedback on the design.”
Call to action
[Screen: Cut back to Host] - CTA must be included **“Finally, Milanote is available for free with no time-limit so sign up for a free Milanote account using the link in the description.”
</aside>
<aside> 🛑 What to avoid in your script
•	Mentioning YouTube Planning: Since many viewers may not be YouTubers, discussing how you use Milanote for YouTube content planning may not be relatable; such as YouTube thumbnail, title, and posting schedule.
•	Neglecting an Introduction: Avoid diving straight into your project without first explaining what Milanote is. Briefly describe “Milanote is a tool for organizing your creative projects.”
•	Sign-Up Instructions: Refrain from mentioning 'downloading' Milanote. Instead, direct users to 'sign up for free.'
•	Forgetting Call to Action: Remember to encourage your viewers to sign up using the link in the description. </aside>"""
# Define the messages
messages = [
    ("system", "You are a helpful assistant that evaluates influencer content submissions against a brand's brief."),
    ("human", prompt.format(brand_brief = brand_brief ,influencer_submission=influncer_sub))
]

# Invoke the LLM
ai_msg = llm.invoke(messages)
print(ai_msg.content)
