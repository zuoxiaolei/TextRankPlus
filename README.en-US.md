# _TextRankPlus_: _more than TextRank algorithm_

Uses the [*word2vec*](https://towardsdatascience.com/introduction-to-word-embedding-and-word2vec-652d0c2060fa) algorithm to compute word spatial distances for keyword extraction and the **Relaxed Word Mover's Distance** (*RWMD*) algorithm for key sentence extraction. Welcome to *star* and contribute code.

![NLP](data/text_rank_coin.png)

# *Python* dependencies
&#160;[networkx>=1.11](http://networkx.github.io/)  
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Build word relationship graphs and calculate word weights  
[gensim>=1.0.1](https://radimrehurek.com/gensim/)   
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;Train *word2vec* models  
[numpy>=1.11.3](https://www.numpy.org/)   
&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;*Python* matrix and tensor computations  
[python2.7](https://www.python.org/) or [python>=3.5](https://www.python.org/)  

## Install dependencies via command line
```bash
pip install -r requirements.txt
```

# Improved *TextRank* usage example
```python
from easynlp import easynlp
raw_text = '''May 12, a special training session on studying and implementing the important expositions of General Secretary Xi Jinping on financial work was held in Beijing. Chen Wenhuai, Deputy Chairman of the China Banking and Insurance Regulatory Commission, made a report on thoroughly implementing General Secretary Xi Jinping's important expositions on financial work, further strengthening insurance supervision, preventing risks in the insurance market, promoting healthy development of the industry, and safeguarding national financial security. Chen Xinqu, Secretary of the Discipline Inspection Commission Attached to the China Banking and Insurance Regulatory Commission, and Huang Hong, Liang Tao, Deputy Chairmen of the China Banking and Insurance Regulatory Commission, attended the meeting.
    Chen Wenhuai pointed out that General Secretary Xi Jinping's important expositions on financial work, especially his important speech at the 40th session of the CPC Central Political Bureau's collective study, are lofty in vision, profound in thought, and comprehensive in content. They are an important component of the new ideas, thoughts, and strategies of the Party Central Committee with Comrade Xi Jinping at the core on governance. They have significant contemporary relevance and far-reaching historical significance. They are fundamental principles and important guidelines for doing financial work well and effectively safeguarding national financial security. The insurance industry should, with high political awareness, deepen learning, enhance understanding, and achieve comprehensive understanding, aligning thoughts and actions with the spirit of General Secretary Xi Jinping's important expositions. They should, from the political height of adhering to the overall national security concept, deeply recognize the extreme importance of safeguarding financial security, and comprehensively enhance the capabilities of financial work under the new circumstances.
    Chen Wenhuai pointed out that it is necessary to deeply recognize the current situation and requirements facing the insurance industry and insurance supervision from the height of safeguarding national financial security. It is necessary to deeply understand the requirements of the central leadership on financial work, raise the political position of insurance work, grasp insurance work under the grand logic of serving the Party Central Committee's governance, and grasp insurance work from the height of safeguarding national security and financial security, finding the right point to promote stable and healthy economic development. It is necessary to advance reforms by taking into account the strengthening and solidification of the Party's ruling capacity, coordinated advancement of the "Four-in-One" strategic layout, and implementation of major central decisions and deployments. We should focus on our core business, return to the fundamental purpose of serving economic development, develop financial insurance undertakings that the Party and people need, and create a good financial environment for the real economy. We should deeply grasp the difficulties and challenges faced by the insurance industry, enhance a sense of crisis and urgency in doing insurance work, adopt a problem-oriented approach, strengthen and improve financial supervision and risk prevention and control work, enhance risk prevention awareness, prepare for emergencies, resolutely govern market malpractices, effectively safeguard the risk bottom line, and resolve and properly dispose of a number of risk points. We should deeply recognize the shortcomings in insurance supervision work, enhance the sense of responsibility and mission in doing insurance supervision, constantly strengthen regulatory system construction, promptly make up for regulatory deficiencies, strive to improve regulatory standards, strengthen regulatory enforcement, profoundly advance anti-corruption and integrity work, and reconstruct a clean political ecosystem in the industry.
    Chen Wenhuai emphasized that learning and implementing the spirit of General Secretary Xi Jinping's important expositions on financial work must adhere to the principle of "making unremitting efforts in both respects." Politically, it means continuing to deepen the "Two Studies and One Doing" learning and education, and using the thoughts of General Secretary Xi Jinping on governance and his important expositions on financial work to arm our minds and guide practice. In business, it means implementing the requirements of General Secretary Xi Jinping on doing financial work well, focusing on the overall principle of "active finance, active economy; stable finance, stable economy," and ensuring the implementation of the "1+4" series of documents recently issued by the China Banking and Insurance Regulatory Commission. In the next step, the insurance regulatory system should resolutely adhere to "the insurance industry serves the interests of insurance, and the regulatory authority performs its supervision duties," and do its best to ensure the implementation of the series of documents. We will resolutely safeguard the bottom line of not causing systemic risks, rectify market malpractices, fill gaps in regulation and the industry, better support the real economy, and build a solid foundation for the stable and healthy development of the insurance industry. At the same time, we should take a strategic overview, strengthen regulatory coordination and arrangement, grasp the intensity and rhythm of regulation, implement specific measures, fully assess the effectiveness of regulatory policies, enhance market analysis and response, provide policy interpretations in a timely manner, stabilize market expectations, and advance related work in a stable and appropriate manner.'''
# Get the sorted keywords and write them to a file
sorted_words = easynlp.get_keyword(raw_text)
print(sorted_words)
```

# Word Cloud Generated by the Model
![Word Cloud](data/tr.png)

# _TODO_
- Keyword extraction based on *BiLSTM* + *CRF*
- Modularization of the *Python* components
- Add *PyPI* support
- Add more NLP modules
- Add lazy import functionality
