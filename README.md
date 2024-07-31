Reddit Analysis

I downloaded the top 1,000 posts (968, to be exact) from this subreddit over the past year. I then used the Groq API and the LLaMA 3 70B model to analyze and classify them into the following categories:

    Engineering (e.g., software doubts or building something)
    Jobs situation (e.g., layoffs, placements)
    Money (e.g., salary, CTC)
    Office politics
    News
    Misc (for posts that don't fit any other category)
    Not enough context (for posts with insufficient information for classification)

Here are the results:

    Engineering: 158 of 968 => 16.32%
    Jobs situation: 371 => 38.32%
    Money: 251 => 26%
    Office Politics: 73 => 7.5%
    News: 44 => 4.5%
    Misc: 28 => 2.9%
    No context: 36 => 3.7%

The classified posts are mostly correct, but there are some discrepancies when I verified manually
