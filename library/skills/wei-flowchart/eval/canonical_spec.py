#!/usr/bin/env python3
"""The end-to-end system map, declared as a graph. Nothing here says where a box goes.

Symbols follow ISO 5807:1985, so a reader who has seen a flowchart before already knows
what each outline means without a legend:

    stadium      start or end of the flow            Candidate, Placement
    rectangle    a process step                      the screening tool, the engine
    diamond      a decision, every exit labelled     does the candidate have a GitHub history
    trapezoid    an operation performed by a person  the interview, the trainer, IRS approval
    cylinder     stored data                         the roadmap catalog
    wavy foot    a document or report                the dashboard, the Skills Passport
    circle       a connector, joining a jump         the weekly loop, the client review loop

Six things Wei found wrong with the hand-placed version, and where each is fixed:

  1 the screening branch never said what it branched on   -> decision diamond, both exits labelled
  2 the trainer edge ran the whole height of the chart    -> connector pair A
  3 a planned-not-live gate dead-ended in the middle      -> cut; it is not part of the live flow
  4 "four written standards" is a code, not a thing       -> the four are named in the box
  5 the client appeared nowhere                           -> the client, upstream and downstream
  6 nothing said which way the loop closed                -> connector pairs carry the two loops
"""
# Every party the chart names, in one place. Retarget the whole map by editing this dict.
# Two forms because one of them lands mid-sentence: "a simulated Client project" is wrong.
VARS = {"Client": "Client", "client": "client"}

SPEC = {
    "vars": VARS,
    "title": "Catalyte AI - end-to-end system map",
    "nodes": [
        # the person, top to bottom
        {"id": "cand", "kind": "terminator", "title": "Candidate",
         "subs": ["sourced by Catalyte", "and Fearless"]},
        {"id": "dec", "kind": "decision", "title": "GitHub history?", "subs": []},
        {"id": "scr", "kind": "process", "title": "Screening tool",
         "subs": ["GitHub and LinkedIn in,", "SkillsGraph scoring"]},
        {"id": "cat2", "kind": "process", "title": "Catalyte assessment",
         "subs": ["aptitude, no code history", "required"]},
        {"id": "int", "kind": "manual", "title": "Interview",
         "subs": ["Catalyte and Fearless"]},
        {"id": "irsg", "kind": "manual", "title": "{Client} batch approval",
         "subs": ["candidate list submitted"]},
        {"id": "appr", "kind": "terminator", "title": "Apprentice",
         "subs": ["onboarded in week 0"]},
        # the weekly cycle
        {"short": "Classroom", "id": "gc", "kind": "process", "title": "Google Classroom",
         "subs": ["the week's assignment"]},
        {"id": "gh", "kind": "process", "title": "GitHub repository",
         "subs": ["source code, AI session logs,", "and the rest of the week's work"]},
        {"id": "eng", "kind": "process", "title": "Assessment engine",
         "subs": ["findings, each carrying", "its evidence"]},
        {"id": "prog", "kind": "process", "title": "Program layer",
         "subs": ["findings placed against", "the cohort"]},
        {"short": "the dashboard", "id": "dsh", "kind": "document", "title": "Cohort dashboard",
         "subs": ["what the trainer and", "the client read"]},
        {"id": "sp", "kind": "document", "title": "Capability Graph",
         "subs": ["what the apprentice reads"]},
        {"short": "the trainer", "id": "tr", "kind": "manual", "title": "Catalyte trainer",
         "subs": ["adjusts the next week"]},
        {"id": "cap", "kind": "manual", "title": "Capstone, then clearance",
         "subs": ["a simulated {client} project"]},
        {"id": "plc", "kind": "terminator", "title": "Placement",
         "subs": ["with the {client}"]},
        # what supplies the cycle
        {"short": "the client", "id": "irs", "kind": "terminator", "title": "{Client}",
         "subs": ["sets the requirements,", "reads the dashboard"]},
        {"id": "std", "kind": "predefined", "title": "Four written standards",
         "subs": ["curriculum, rubrics,", "content sourcing, personas"]},
        {"id": "cur", "kind": "predefined", "title": "Curricula",
         "subs": ["domains, competencies,", "modules"]},
        {"id": "rub", "kind": "document", "title": "Project rubrics",
         "subs": ["126 and 172 checkpoints"]},
        {"id": "rcat", "kind": "datastore", "title": "Roadmap catalog",
         "subs": ["65 roadmaps,", "1,349 checkpoints"]},
    ],
    "edges": [
        ("cand", "dec"),
        ("dec", "scr", "has one"),
        ("dec", "cat2", "has none"),
        ("scr", "int"), ("cat2", "int"),
        ("int", "irsg"), ("irsg", "appr"), ("appr", "gc"),
        ("gc", "gh"), ("gh", "eng"), ("eng", "prog"),
        ("prog", "dsh"), ("prog", "sp"), ("prog", "cap"), ("cap", "plc"),
        ("dsh", "tr"),
        ("tr", "gc"),          # closes the weekly loop  -> connector pair
        ("dsh", "irs"),         # closes the client loop  -> connector pair
        ("irs", "std"), ("std", "cur"), ("std", "rub"),
        ("cur", "gc"), ("rub", "eng"), ("rcat", "eng"),
    ],
    # the two edges that close a loop. Declared, not guessed -- see layout.layout().
    "feedback": [("tr", "gc"), ("dsh", "irs")],
}
