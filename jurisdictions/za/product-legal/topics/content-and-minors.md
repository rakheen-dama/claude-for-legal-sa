# Content and Minors — South African Framework

This overlay covers the Films & Publications Act 65 of 1996, Children's Act 38 of 2005, POPIA children's data provisions, gambling/gamification regulation, and online safety obligations. It is conditionally loaded by launch-review (children/gaming sectors) and feature-risk-assessment skills when jurisdiction = ZA and product touches children, content, or gaming.

---

## 1. Films & Publications Act framework

### Content classification

The Films & Publications Act establishes a mandatory content classification system administered by the Film and Publication Board (FPB). All films, games, and certain publications distributed in South Africa must be classified before distribution.

Classification categories:

| Rating | Meaning | Restriction |
|---|---|---|
| A | All ages | None |
| PG | Parental guidance | Advisory — not restricted |
| 7-9PG | Not suitable for children under 7-9; parental guidance | Advisory |
| 10 | Not suitable for children under 10 | Advisory |
| 10-12PG | Not suitable for children under 10-12; parental guidance | Advisory |
| 13 | Not suitable for children under 13 | Restricted |
| 16 | Not suitable for persons under 16 | Restricted — age verification required |
| 18 | Not suitable for persons under 18 | Restricted — age verification required |
| X18 | Restricted to adults only | May only be distributed through licensed premises |
| XX | Refused classification — prohibited | Distribution is a criminal offence |

### Online content amendments (2019)

The Films and Publications Amendment Act 11 of 2019 extended the classification framework to online content:

- **Online distributors** must register with the FPB if they distribute or exhibit content to the public in South Africa.
- **Content that must be classified** includes films, games, and certain user-generated content that contains classifiable elements (violence, sexual content, language, drug use).
- **Pre-classification exemption** — certain categories of online content are exempt from pre-classification but remain subject to complaint-driven classification.

### Age-gating obligations

Platforms distributing classified content must implement age-gating mechanisms appropriate to the classification:

- Content rated 16 or 18 — age verification before access.
- Content rated X18 — distribution only through licensed premises (physical or online equivalent with robust age verification).
- The FPB has not prescribed specific age verification technology, but the obligation is to take reasonable steps to prevent minors from accessing restricted content.

### Takedown obligations

Online platforms must comply with takedown procedures for:

- Content classified XX (prohibited).
- Child sexual abuse material (CSAM) — zero tolerance; immediate removal and reporting to SAPS and FPB.
- Revenge pornography / non-consensual intimate images — criminalised under the Cybercrimes Act.

---

## 2. Children's Act obligations

### Best interests standard

The Children's Act 38 of 2005 establishes that the best interests of the child are paramount in all matters concerning the child (s9). This constitutional standard applies to product design decisions affecting children.

### Parental consent and capacity

- A child is any person under the age of 18 (Children's Act s1).
- Children have evolving capacity — the Act recognises that children of different ages have different levels of understanding and decision-making ability.
- For significant decisions affecting children, the consent of a parent, guardian, or care-giver is required.
- This intersects with POPIA's "competent person" concept (see section 3 below).

### Reporting obligations

Any person who has knowledge, reasonable belief, or suspicion that a child has been abused or is in need of care and protection must report this to a designated child protection organisation, the provincial Department of Social Development, or a police official (s110). This obligation applies to platform operators who become aware of child exploitation through their systems.

---

## 3. POPIA children's data (s34-35)

### Special processing conditions

POPIA imposes heightened requirements for processing personal information of children:

- **Definition of child** — a natural person under the age of 18 years who is not legally competent, without the assistance of a competent person, to take any action or decision in respect of any matter concerning him- or herself (s1).
- **Prohibition** — processing of a child's personal information is prohibited unless specific conditions are met (s34).
- **Competent person consent** — processing is permitted if a competent person (parent, guardian, or other person with legal authority) consents on behalf of the child (s35(1)(a)).
- **Other grounds** — processing may also be permitted if necessary to comply with an obligation of international public law, for historical, statistical, or research purposes, or if the information was deliberately made public by the child with consent of a competent person.

### Prior authorisation from Information Regulator

Certain processing of children's data requires prior authorisation from the Information Regulator before processing begins (s57(1)(c)). This applies to processing that does not meet the standard conditions and requires the responsible party to submit an application and receive authorisation.

### Practical implications for product design

- **Age screening** — products accessible to children must implement mechanisms to identify child users and obtain competent person consent before processing their personal information.
- **Consent architecture** — the consent mechanism must be designed to obtain verifiable consent from a competent person, not merely the child clicking "I agree."
- **Data minimisation** — heightened obligation to collect only the minimum personal information necessary when the data subject is a child.
- **Purpose limitation** — personal information of children must not be processed for purposes beyond what was consented to, particularly for marketing, profiling, or behavioural targeting.

---

## 4. Gambling and gamification

### National Gambling Act 7/2004

The National Gambling Act establishes a closed list of permitted gambling activities in South Africa:

- Casino games (licensed by provincial boards).
- Horse racing and betting (licensed by provincial boards).
- Limited payout machines (licensed by provincial boards).
- Bingo (licensed by provincial boards).
- Sports betting (licensed by provincial boards).
- National lottery (operated under the Lotteries Act by licence from the NLB).

### Online gambling prohibition

Online gambling is prohibited in South Africa. The Interactive Gambling Regulations (2008) prohibit operators from offering gambling through interactive communications, and persons from participating in such gambling. While enforcement has been inconsistent, the legal position is clear: offering online gambling to SA users is unlawful.

### Loot box risk analysis framework

Loot boxes and similar randomised in-game purchase mechanics occupy a grey area under SA law. The analysis turns on whether the mechanic constitutes "gambling" under the National Gambling Act:

| Element | Gambling Act definition | Loot box analysis |
|---|---|---|
| **Consideration** | Payment or stake | Purchase price of loot box = consideration |
| **Chance** | Outcome determined by chance | Randomised contents = chance element |
| **Prize** | Money or money's worth | In-game items with no cash-out = weaker; tradeable/sellable items = stronger |

If loot box contents can be traded, sold, or converted to real-world value, the mechanic more closely resembles gambling. If contents are purely cosmetic and non-transferable, the gambling classification is weaker but not eliminated.

### Prize mechanics

Any mechanic where users pay to participate and may win prizes of value must be assessed against:

1. **National Gambling Act** — is this gambling? (Closed list; if yes, requires provincial licence.)
2. **Lotteries Act** — is this an unlawful lottery? (Consideration + chance + prize = lottery.)
3. **CPA s36** — can this be structured as a lawful promotional competition? (Free entry + rules + disclosure = lawful.)

The safest approach: ensure a genuine free entry method, comply with CPA s36, and avoid any mechanic that requires payment for a chance to win.

---

## 5. Online safety features

### Protection from Harassment Act 17/2011

The Act allows victims of harassment, including cyberbullying and online harassment, to obtain protection orders from a Magistrate's Court. Platforms must:

- Provide accessible reporting mechanisms for harassment.
- Cooperate with court orders requiring disclosure of user information or removal of content.
- Consider implementing proactive blocking and muting features.

### Cybercrimes Act 19/2020 — harmful communications

The Cybercrimes Act criminalises the disclosure of harmful data messages, including:

- Messages inciting damage to property or violence (s14).
- Non-consensual sharing of intimate images (s16).
- Messages intended to cause harm to a person identified or identifiable from the message.

Platforms hosting user-generated content must implement:

- **Reporting tools** — accessible mechanism for users to report harmful content.
- **Blocking capabilities** — users must be able to block other users.
- **Moderation processes** — content review and removal procedures for reported content.
- **Cooperation with law enforcement** — processes for responding to SAPS requests and court orders under the Cybercrimes Act.

### Platform design considerations

Products directed at or accessible to children should implement safety-by-design principles:

- Default privacy settings (profiles not publicly visible).
- Restricted direct messaging capabilities for minor users.
- Content filtering appropriate to the user's age.
- Parental controls and oversight mechanisms.
- Clear and accessible reporting mechanisms designed for children.
- Response protocols for CSAM discovery (immediate removal, FPB and SAPS notification).
