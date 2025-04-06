import * as React from "react";
import { MD3LightTheme, PaperProvider, useTheme } from "react-native-paper";
import BottomNavigationBar from "./navigation/BottomNavigation";

const theme = {
  ...MD3LightTheme,
  custom: "property",
  colors: {
    ...MD3LightTheme.colors,
    primary: "#EC5F5F",
    background: "#FFFFFF",
    brandPrimary: "#fefefe",
    brandSecondary: "red",
  },
};

export type AppTheme = typeof theme;

export const useAppTheme = () => useTheme<AppTheme>();

export default function App() {
  return (
    <PaperProvider theme={theme}>
      <BottomNavigationBar />
    </PaperProvider>
  );
}
