import React from "react";
import { ScrollView, StyleSheet, TextInput, View } from "react-native";
import { Appbar, Button, Text } from "react-native-paper";

const Header = () => (
  <Appbar.Header>
    <Appbar.Content title="Find a ride" />
  </Appbar.Header>
);

const HomeScreen = () => (
  <View style={styles.container}>
    <Header />
    <ScrollView contentContainerStyle={styles.content}>
      <Text style={styles.subheading}>Where are you going?</Text>
      <TextInput style={styles.input} placeholder="From" />
      <TextInput style={styles.input} placeholder="To" />
      <Text style={styles.subheading}>When to leave?</Text>
      <TextInput style={styles.input} placeholder="Select date and time" />
    </ScrollView>
    <Button
      mode="contained"
      style={styles.button}
      onPress={() => console.log("Search Rides pressed")}
    >
      Search Rides
    </Button>
  </View>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  content: {
    flexGrow: 1,
    padding: 16,
  },
  subheading: {
    fontSize: 18,
    marginVertical: 8,
  },
  input: {
    width: "90%",
    height: 50,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    paddingHorizontal: 12,
    marginVertical: 8,
  },
  button: {
    width: "90%",
    alignSelf: "center",
    marginVertical: 16,
    position: "absolute",
    bottom: 16,
  },
});

export default HomeScreen;
