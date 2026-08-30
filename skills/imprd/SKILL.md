---
name: imprd
description: Iterative Multi-Perspective Rhetorical Debugging. Evaluate and refine a piece of writing by generating reader personas drawn from its actual target audience, scoring six dimensions, running five audits, and iterating to convergence. Use when asked to run IMPRD, critique a draft rigorously, or harden writing against hostile readers.
---

# IMPRD — Iterative Multi-Perspective Rhetorical Debugging

**This is a thinking methodology you execute, not a program you run.** There is no
script. You generate the personas, inhabit each one, score, audit, revise, and
repeat until convergence.

**Run it to completion.** Do not stop after one scoring pass and report numbers.
One pass is a diagnosis; IMPRD is the treatment. Iterate — score, revise, rescore
— until the convergence test below is met or the six-iteration cap is reached.
Report the trajectory, not a snapshot.

Full kernel, authoritative for anything not covered here:
`~/repos/conceptual-refinement/methodologies/iterative-multi-perspective-rhetorical-debugging-v1.1.0-runtime.md`

---

## 0. Manipulation audit — VETO POWER

Before anything else. **Stop and refuse** if the piece:

- contains false or misleading factual claims
- exploits fear, outrage or anxiety to move the reader rather than to inform
- targets vulnerable people for exploitation
- is propaganda or coordinated inauthentic content
- is *about* a marginalised community without that community's involvement

Legitimate emotional appeal is factually framed, acknowledges trade-offs, and
respects the reader's autonomy. Manipulation misleads, oversimplifies to trigger,
and manufactures urgency.

**You cannot optimise the persuasiveness of something false.** Improving the
rhetoric of a false claim compounds the harm. If the audit fails, say so and stop.

---

## 1. Content analysis — do this before generating personas

Write these down explicitly. Everything downstream depends on them.

- **Primary message** — the core claim in one sentence
- **Target audience** — specific, not "general readers." Who actually reads this?
  What do they already know? What will they resist?
- **Intended action** — what should the reader think, feel or do afterwards?
- **Stakes** — LOW (personal), MEDIUM (professional platform), HIGH (affects
  policy, contested social claims, or vulnerable groups)
- **Content type** — persuasive, informational, exploratory? Decides which
  dimensions apply.
- **The author's distinctive voice** — what must survive optimisation. If a voice
  document exists, use it.

**At HIGH stakes, persona simulation is not sufficient.** Say so in the report and
recommend real readers before publication.

---

## 2. Build the persona pool FROM THE AUDIENCE

**Do not use a fixed roster.** A standing cast produces local minima and starts
scoring the same way every time. Derive the pool from the content analysis above.

Generate **15–20 personas**, then randomly sample an **odd number (7, 9 or 11)**
for each iteration. Resample each iteration.

The pool must span:

- **The actual target reader**, in two or three variants — the enthusiast, the
  sceptic, the person who half-agrees
- **Adjacent audiences** who might encounter it
- **Domain experts** relevant to the piece's claims. A piece citing statistics
  needs a statistician. A theological piece needs someone who will check the
  exegesis. A technical piece needs a practitioner.
- **Accessibility personas — always, and always weighted 1.5×.** At minimum: a
  non-native speaker, an attention-limited reader, and a reader using assistive
  technology. Accessibility is a requirement, not an optimisation target.
- **The machine-tell critic — always, weighted 1.2×.** See section 5.
- **Hostile readers — always, and see section 3.**

## 3. Hostile readers are mandatory, and they are there to harden the piece

Include at least two personas who want the argument to fail, drawn from whoever
would actually attack this piece. Not strawmen — the most capable opponent the
work will meet.

**Their job is not to be satisfied.** It is to find the specific sentence they
would quote out of context, the weakest citation, the unearned inference, the
place where the author's own standard is not applied to the author. Score the
piece on how well it *survives* them, not on whether they liked it.

Ask each hostile persona:

- What is the single line you would screenshot to discredit this?
- Which claim would you check first, expecting to find it wrong?
- Where does the author demand more rigour from opponents than from himself?
- What would you accuse the author of, and does the text already answer it?

Anything they find that the text does not already answer is a required fix.

---

## 4. Score six dimensions, 1–10, per persona

1. **Understandability** — core message graspable? examples clear? terms defined?
2. **Style quality** — engaging? tone fits? pacing? memorable phrasing?
3. **Human voice** — does a person sound like they wrote this, or does it read as
   generated, corporate, or committee-written?
4. **Forward-ability** — would this persona share it? is there a quotable hook?
   (Skip for content where sharing is not a goal.)
5. **Persuasiveness** — is the argument moving? are objections met? is the author
   trusted? (Skip for purely exploratory content.)
6. **Voice fidelity** — does it still sound like *this author*? Score against the
   author's voice document if one exists. **Weight 1.4× — the heaviest single
   weight**, because a piece that reads as generic has failed regardless of its
   other scores.

Plus, per persona: specific strengths and weaknesses, emotional response, sharing
likelihood and to whom, one highest-impact improvement, and confidence (1–10).

**Weighting:** target audience 1.5×, adjacent 1.0×, far outlier 0.7×;
accessibility 1.5×; deep reader 1.2×; skimming reader 1.3×; multiply by
confidence.

---

## 5. The machine-tell critic — always in the sample

This reader assumes the text was generated and looks for evidence. The question
is not "is this good writing" but "what shows a human wrote it."

Hunts for: relentless parallelism and tricolons; a bolded key sentence in every
section; even section architecture; signposting that announces insight instead of
delivering it ("here's why," "what matters is"); an authentic move repeated until
it becomes a tic; no digression anywhere; anecdotes with no names, places or
dates; stilted seams left by bulk edits; suspiciously uniform hedging.

**Reports a count, not an impression.**

**Note the asymmetry:** a model running this persona on its own output is the
weakest reader in the pool, because the tells are its own defaults. Treat the
score as a ceiling, not a floor, and say so in the report.

---

## 6. Hard requirements — these block convergence

- Every accessibility persona scores **≥7 on understandability**
- Mean human voice **≥7**
- Mean voice fidelity **≥7**
- No target or adjacent persona below **3 on understandability**
- No hostile-persona finding left unanswered in the text

**Red flags:** mean forward-ability below 5 where sharing is a goal; multiple
personas citing the same confusion; **authenticity or voice scores declining
across iterations**, which means over-optimisation.

**Minority report:** up to three personas with specific high-severity concerns are
preserved even when outvoted. Record them.

---

## 7. Five audits, every iteration

**A. Accessibility (must pass).** Reading level, jargon density, sentence
complexity, information density, scanability, structure for neurodiverse readers.
Failure requires revision — this is not a trade-off against other dimensions.

**B. Authenticity vs optimisation.** Is the voice surviving? Are the suggested
changes making it generic? **When optimisation conflicts with authenticity, bias
to authenticity.**

**C. Persuasion pattern.** Are claims confidence-calibrated rather than
overstated? Is emotional appeal legitimate? Is credibility established?
Are counter-arguments answered rather than mentioned?

**D. Viral mechanics** (only where sharing is a goal). Hook in the first two
paragraphs? Two or three quotable lines? Title accurate as well as compelling?
Stakes articulated? Does sharing signal something the sharer wants to signal?

**E. Accuracy and precision.** Are the factual claims true? Sources cited and
read? Is technical precision intact? **Accuracy outranks persuasiveness — always.**

---

## 8. Revise, then iterate

Apply changes with **>70% weighted support**. Preserve minority reports. Then
resample personas and score again.

**Convergence is not a number.** It is:

- **stability** — scores substantively unchanged across two consecutive iterations
- **hard requirements met** — all of them
- **no decline** — nothing going backwards

**A declining score means the previous iteration was the peak. Revert to it.**

Cap at **six iterations**. If not converged by then, report what is blocking and
stop rather than grinding.

---

## 9. Report

Per iteration: personas sampled, all scores with confidence, weight calculations,
findings from all five audits, changes made with rationale, preserved minority
reports, and the score trajectory.

State plainly whether it converged, and if not, what blocked it.

At MEDIUM stakes and above, commit the report alongside the work.
