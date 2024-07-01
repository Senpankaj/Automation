import re
import nltk
from nltk.tokenize import sent_tokenize

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')

# Function to preprocess text
def preprocess_text_nltk(text):
    # Split text into paragraphs based on double newlines
    paragraphs = text.split('\n\n')
    
    processed_text = []
    current_heading = None
    
    for paragraph in paragraphs:
        # Tokenize paragraphs into sentences
        sentences = sent_tokenize(paragraph)
        
        for sentence in sentences:
            # Detect and extract headings using regular expression
            if re.match(r'^[0-9]+\.\s', sentence):  # Matches sections like 2.
                current_heading = f"## {sentence.strip()}"
                processed_text.append(current_heading)
            elif re.match(r'^[0-9]+\.[0-9]+\.?\s', sentence):  # Matches subsections like 2.1 or 2.1.
                current_heading = f"## {sentence.strip()}"
                processed_text.append(current_heading)
            elif re.match(r'^[A-Z]+\.', sentence):  # Matches headings like Abstract, Introduction, etc.
                current_heading = f"# {sentence.strip()}"
                processed_text.append(current_heading)
            else:
                if current_heading:
                    processed_text.append(sentence.strip())
        
        # Add a blank line between paragraphs
        processed_text.append("")
    
    # Join processed text into a single string
    processed_text = "\n".join(processed_text)
    
    return processed_text

# Example usage
text = """
Machine Learning that Matters

Kiri L. Wagstaff

Jet Propulsion Laboratory, California Institute of Technology, 4800 Oak Grove Drive, Pasadena, CA 91109 USA

Abstract

Much of current machine learning (ML) research has lost its connection to problems of
import to the larger world of science and society. From this perspective, there exist glaring limitations in the data sets we investigate, the metrics we employ for evaluation,
and the degree to which results are communicated back to their originating domains.
What changes are needed to how we conduct research to increase the impact that ML
has? We present six Impact Challenges to explicitly focus the field’s energy and attention,
and we discuss existing obstacles that must
be addressed. We aim to inspire ongoing discussion and focus on ML that matters.

1. Introduction

At one time or another, we all encounter a friend,
spouse, parent, child, or concerned citizen who, upon
learning that we work in machine learning, wonders
“What’s it good for?” The question may be phrased
more subtly or elegantly, but no matter its form, it gets
at the motivational underpinnings of the work that we
do. Why do we invest years of our professional lives
in machine learning research? What difference does it
make, to ourselves and to the world at large?
Much of machine learning (ML) research is inspired
by weighty problems from biology, medicine, finance,
astronomy, etc. The growing area of computational
sustainability (Gomes, 2009) seeks to connect ML advances to real-world challenges in the environment,
economy, and society. The CALO (Cognitive Assistant
that Learns and Organizes) project aimed to integrate
learning and reasoning into a desktop assistant, potentially impacting everyone who uses a computer (SRI
International, 2003–2009). Machine learning has effectively solved spam email detection (Zdziarski, 2005)
and machine translation (Koehn et al., 2003), two
problems of global import. And so on. 

And yet we still observe a proliferation of published
ML papers that evaluate new algorithms on a handful
of isolated benchmark data sets. Their “real world”
experiments may operate on data that originated in
the real world, but the results are rarely communicated
back to the origin. Quantitative improvements in performance are rarely accompanied by an assessment of
whether those gains matter to the world outside of
machine learning research.
This phenomenon occurs because there is no
widespread emphasis, in the training of graduate student researchers or in the review process for submitted
papers, on connecting ML advances back to the larger
world. Even the rich assortment of applications-driven
ML research often fails to take the final step to translate results into impact.
Many machine learning problems are phrased in terms
of an objective function to be optimized. It is time for
us to ask a question of larger scope: what is the field’s
objective function? Do we seek to maximize performance on isolated data sets? Or can we characterize
progress in a more meaningful way that measures the
concrete impact of machine learning innovations?

2. Machine Learning for Machine
Learning’s Sake

This section highlights aspects of the way ML research
is conducted today that limit its impact on the larger
world. Our goal is not to point fingers or critique individuals, but instead to initiate a critical self-inspection
and constructive, creative changes. These problems do
not trouble all ML work, but they are common enough
to merit our effort in eliminating them.
The argument here is also not about “theory versus
applications.” Theoretical work can be as inspired by
real problems as applied work can. The criticisms here
focus instead on the limitations of work that lies between theory and meaningful applications: algorithmic advances accompanied by empirical studies that
are divorced from true impact.

2.1. Hyper-Focus on Benchmark Data Sets

Increasingly, ML papers that describe a new algorithm
follow a standard evaluation template. After presenting results on synthetic data sets to illustrate certain
aspects of the algorithm’s behavior, the paper reports
results on a collection of standard data sets, such as
those available in the UCI archive (Frank & Asuncion,
2010).

2.2. Hyper-Focus on Abstract Metrics

There are also problems with how we measure performance. Most often, an abstract evaluation metric
(classification accuracy, root of the mean squared error or RMSE, F-measure (van Rijsbergen, 1979), etc.)
is used. These metrics are abstract in that they explicitly ignore or remove problem-specific details, usually so that numbers can be compared across domains.
"""

processed_text = preprocess_text_nltk(text)
print(processed_text)
