FROM maven:3.8.6-jdk-11-slim as builder
WORKDIR /app3
COPY . /app3/
RUN mvn clean package

FROM openjdk:11-slim as runtime
COPY --from=builder app3/target/app3-0.0.1-SNAPSHOT.jar /app/app3.jar
EXPOSE 8010
RUN addgroup --system docker && useradd --system --group docker duser
USER duser
ENTRYPOINT ["java","-jar","app/app3.jar", "--server.port=8010"]