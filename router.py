from semantic_router import Route, RouteLayer # few versions after RouteLayer changed to SemanticRouter
from semantic_router.encoders import CohereEncoder
import os
import dotenv

dotenv.load_dotenv()

os.environ["COHERE_API_KEY"] = "Y1XLkXM3vEE0STFFTmzm4lawU0xXBBJujJjw1aXZ"
encoder = CohereEncoder()

faq = Route(
    name = 'faq',
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "Why am I unable to order products like television, air-conditioner, refrigerator, washing machine, furniture, microwave, treadmill, etc. at my location?",
        "What should I do if my order is approved but hasn't been shipped yet?",
        "Can I take the shipment after opening and checking the contents inside?",
        "How quickly can I get my order delivered?",
        "What are the standard shipping speeds and delivery charges?",
        "When will I get my order once its status changes to 'Out for Delivery'?",
    ],
)

sql = Route(
    name = 'sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ],
)

small_talk = Route(
    name = 'small-talk',
    utterances=[
        "Hi",
        "How are you?",
        "What is your name?",
        "Are you a robot?",
        "What are you?",
        "What do you do?",
        "Let's talk",
    ],
)

router = RouteLayer(encoder=encoder, routes = [faq, sql, small_talk])