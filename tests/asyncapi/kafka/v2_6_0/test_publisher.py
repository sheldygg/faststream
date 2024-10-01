from faststream.kafka import KafkaBroker
from faststream.specification.asyncapi import AsyncAPI
from tests.asyncapi.base.v2_6_0.publisher import PublisherTestcase


class TestArguments(PublisherTestcase):
    broker_class = KafkaBroker

    def test_publisher_bindings(self):
        broker = self.broker_class()

        @broker.publisher("test")
        async def handle(msg): ...

        schema = AsyncAPI(self.build_app(broker), schema_version="2.6.0").to_jsonable()
        key = tuple(schema["channels"].keys())[0]  # noqa: RUF015

        assert schema["channels"][key]["bindings"] == {
            "kafka": {"bindingVersion": "0.4.0", "topic": "test"}
        }