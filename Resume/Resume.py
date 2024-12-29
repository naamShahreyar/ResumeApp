
import reflex as rx

from rxconfig import config
from .Utils import Neo4jHandler, find_candidates_with_skills, get_candidate, HuggingFaceEmbeddingModel
from langchain.vectorstores.neo4j_vector import Neo4jVector
from .params import Neo4j_params
from .Secrets import Neo4j_url, Neo4j_username, Neo4j_password   

# Neo4j configuration
neo4j_handler = Neo4jHandler(Neo4j_url, Neo4j_username,Neo4j_password)
neo4j_vector_index = Neo4jVector.from_existing_graph(
    HuggingFaceEmbeddingModel,
    url=Neo4j_url,
    username=Neo4j_username,
    password=Neo4j_password,
    index_name=Neo4j_params['Neo4j_index_name'],
    node_label=Neo4j_params['Neo4j_node_label'],
    text_node_properties=Neo4j_params['Neo4j_text_node_properties'],
    embedding_node_property=Neo4j_params['Neo4j_embedding_node_property'],
)
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
