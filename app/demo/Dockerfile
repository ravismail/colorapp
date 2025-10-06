# Use JDK to build
#FROM maven:3.9.6-eclipse-temurin-17 AS build
#WORKDIR /app
#COPY pom.xml .
#COPY src ./src
#RUN mvn clean package -Dmaven.test.skip=true

# Use lightweight JRE to run
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
#COPY --from=build /app/target/color-demo-0.0.1-SNAPSHOT.jar app.jar
COPY  target/color-demo-0.0.1-SNAPSHOT.jar app.jar

# Expose app port
EXPOSE 8080

# Run with dynamic color
ENTRYPOINT ["java", "-jar", "app.jar"]
